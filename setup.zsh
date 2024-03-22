#!/bin/zsh


# Checking if the virtual envirement in installed
check_virtualenv() {
    if ! command -v virtualenv &> /dev/null; then
        echo "virtualenv is not installed.\nInstalling..."
        pip3 install virtualenv
    else
        echo "virtualenv installation is already installed."
    fi
}

# Check if the .venv is present and install
# the requirements if they are not installed
create_venv() {
    # check_virtualenv
    if [ -d ".venv" ]; then
        echo "Virtual environment '.venv' already exists. Aborting."
        # return 1
    fi
    python3 -m venv ".venv"
    source .venv/bin/activate
    pip3 install --upgrade pip
    pip3 install -r plogReq.txt
}

# check if the alias is already mantioned in the .zshrc file if not added it
add_alias () {
    $(cat $HOME/.zshrc | grep "alias plog='python3 $HOME/.tools/plog/main.py'")
    if [[ $? -eq 1 ]]; then
        echo 'alias plog="python3 $HOME/.tools/plog/main.py"' >> $HOME/.zshrc
        cat $HOME/.zshrc
    fi
}

PTH="$HOME/.tools/plog"

mkdir -p "$PTH"

cp * "$PTH"/

create_venv

add_alias

source $HOME/.zshrc

source .venv/bin/activate
