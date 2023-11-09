#!/bin/bash -ex

# configure bashrc ----------------------

if [ "$(cat ~/.bashrc)" == "" ]; then
    cat /etc/skel/.bashrc > ~/.bashrc
fi

cat >> ~/.bashrc << EOF

#--- custom setttings ---

export PATH=\$PATH:~/.local/bin

export JAVA_HOME=/usr/lib/jvm/java-19-openjdk-amd64
EOF

# python libraries ----------------------

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install --user \
    numpy matplotlib pandas scipy scikit-learn seaborn \
    jupyterlab notebook \
    tqdm click typer requests \
    black ruff
