#!/bin/bash

if ! command -v poetry &> /dev/null
then
    echo "Poetry is not found. Please install poetry and try again."
    exit
fi

if ! command -v pipx &> /dev/null
then
    echo "pipx is not found. Please install pipx and try again."
    exit
fi

if pipx list | grep -q assistant-bot; then
    echo "assistant-bot is already installed."
    read -p "Press any key to continue..."
    exit
fi

echo "Building distribution package with poetry..."
poetry build

WHL_FILE=$(ls dist/*.whl)
echo "Installing the package with pipx..."
pipx install "$WHL_FILE"

echo "Installation complete. You can now run the bot with the assistant-bot command from anywhere in the system."
read -p "Press any key to continue..."
