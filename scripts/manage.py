#!/usr/bin/env python3

from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass
import re

import pandas as pd
import typer

cli = typer.Typer()


@dataclass
class Student:
    序号: int
    姓名: str
    学号: str
    邮箱: str
    电话: str
    专业方向: str


def load_students_csv(path: Path):
    df = pd.read_csv(path)
    df["学号"] = df["学号"].astype(str)
    return df


@cli.command()
def print_students(path: Path):
    df = load_students_csv(path)
    print(df.to_string(index=False, col_space=[4, 8, 12, 32, 12, 6]))


def load_students_list(path: Path) -> List[Student]:
    df = load_students_csv(path)
    return [Student(**row.to_dict()) for _, row in df.iterrows()]


def assign_ports(stu: Student) -> List[Tuple[int, int]]:
    assert 1 <= stu.序号 < 100
    start = 10000 + stu.序号 * 10  # 10xx0 ~ 10xx9
    ports = [(start + i, start + i) for i in range(10)]
    ports[0] = (ports[0][0], 22)  # 1st: ssh
    ports[1] = (ports[1][1], 80)  # 2nd: http
    return ports


@cli.command()
def start(students_path: Path, image: str):
    students = load_students_list(students_path)

    print("#!/bin/bash -ex")
    print("mkdir -p /mair/data/shared")
    print("chown -R 1000:1000 /mair/data/shared")
    print()

    for stu in students:
        # data dir
        assert re.match(r"^\d{9}$", stu.学号)
        src_data_dir = f"/mair/data/{stu.学号}"
        dst_data_dir = f"/data/{stu.学号}"
        print(f"mkdir -p {src_data_dir}")
        print(f"chown -R 1000:1000 {src_data_dir}")

        # docker run
        mounts = [
            f"--mount type=bind,source={src_data_dir},target={dst_data_dir}",
            "--mount type=bind,source=/mair/data/shared,target=/data/shared",
        ]
        ports = [f"-p 0.0.0.0:{a}:{b}" for a, b in assign_ports(stu)]
        names = [f"--hostname {stu.学号}", f"--name {stu.学号}"]
        gpus = ["--runtime=nvidia", "--gpus all"]
        cmd = ["docker run", *ports, *mounts, *names, *gpus, "-d", image]
        print(" ".join(cmd))
        print()


@cli.command()
def stop(students_path: Path):
    students = load_students_list(students_path)
    print("#!/bin/bash -ex")
    for stu in students:
        print(f"echo '序号: {stu.序号}'")
        print(f"docker stop {stu.学号}")


@cli.command()
def set_password(students_path: Path):
    students = load_students_list(students_path)
    for stu in students:
        # set default password
        print(f"docker container exec -u 0 {stu.学号} bash -c 'echo mair:{stu.电话} | chpasswd'")
    print()


@cli.command()
def ssh_test(students_path: Path):
    students = load_students_list(students_path)
    print("#!/bin/bash -ex")
    for stu in students:
        ssh_port = assign_ports(stu)[0][0]
        cmd = f"echo test > {stu.学号}.txt"
        print(f"echo '{cmd}' | sshpass -p {stu.电话} ssh -o StrictHostKeyChecking=no -p {ssh_port} mair@localhost")


if __name__ == "__main__":
    cli()
