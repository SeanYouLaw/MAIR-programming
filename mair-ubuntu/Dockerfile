FROM ubuntu:22.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# setup apt
RUN pwd \
    && sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g    /etc/apt/sources.list \
    && sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g   /etc/apt/sources.list \
    && apt clean \
    && apt update \
    && apt upgrade -y \
    && apt autoremove

RUN apt install -y \
        # basic tools
        sudo vim git curl wget net-tools ca-certificates gnupg  \
        # basic services
        openssh-server \
        # extra tools
        htop \
        # C++ toolchain
        build-essential gdb cmake autoconf \
        clang clang-format clang-tidy clang-tools clangd lld \
        # Python toolchain
        python3 python3-pip python-is-python3 \
        # Java toolchain
        openjdk-19-jdk openjdk-19-doc openjdk-19-dbg

# FIXME: https://bugs.launchpad.net/cloud-images/+bug/1996489
# RUN yes | unminimize

COPY vendor /vendor
COPY vendor.sh /vendor.sh
RUN  /vendor.sh install-root

RUN pwd \
    && USER_PASSWORD='mair!20231024' \
    && useradd -m -s /bin/bash -G sudo -p "$(openssl passwd -1 $USER_PASSWORD)" mair

COPY user.sh /user.sh

USER mair
RUN  /user.sh
RUN  /vendor.sh install-user

USER root
RUN  rm /user.sh /vendor.sh && rm -rf /vendor

EXPOSE 22
CMD ["service", "ssh", "start", "-D"]
