#!/bin/zsh

PTH="$HOME/.tools/plog"

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
    if [ -d "$PTH/.venv" ]; then
        echo "Virtual environment '.venv' already exists. Aborting."
        return 1
    fi
    python3 -m venv "$PTH/.venv"
    source "$PTH/.venv/bin/activate"
    pip3 install --upgrade pip
    pip3 install -r "$PTH/plogReq.txt"
}

# check if the alias is already mantioned in the .zshrc file if not added it
add_alias () {
    grep 'alias plog="zsh $HOME/.tools/helper/plog/run.sh"' < $HOME/.zshrc 
    if [[ $? -eq 1 ]]; then
        echo 'alias plog="zsh $HOME/.tools/plog/helper/run.sh"' >> $HOME/.zshrc
        source $HOME/.zshrc
    fi
}

set_dir() {
    if [[ ! -d "$PTH" ]]; then
        mkdir -p "$PTH"
        cp * "$PTH"/
    fi
}

set_dir > /dev/null

create_venv > /dev/null

add_alias > /dev/null

