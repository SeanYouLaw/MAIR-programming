#!/bin/bash -ex

# before docker build
if [ "$1" == "download" ]; then
    mkdir -p vendor
    cd vendor

    wget --output-document ripgrep.deb \
        https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep_13.0.0_amd64.deb
    wget --output-document fd.deb \
        https://github.com/sharkdp/fd/releases/download/v8.7.1/fd_8.7.1_amd64.deb

    mkdir -p pip
    cd pip
    pip3 download torch torchvision torchaudio
fi

# during docker build
if [ "$1" == "install-root" ]; then
    cd vendor
    
    dpkg -i ripgrep.deb
    dpkg -i fd.deb
    ln -s "$(which fd)" /usr/local/bin/fd
fi

# during docker build
if [ "$1" == "install-user" ]; then
    cd vendor

    pip install --user --no-index --find-links="./pip" \
        torch torchvision torchaudio
fi

if [ "$1" == "" ]; then 
    exit 1
fi
