#!/bin/bash

if ! pipx list | grep -q assistant-bot; then
    echo "assistant-bot is not installed."
    read -p "Press any key to continue..."
    exit
fi

echo "Uninstalling assistant-bot using pipx..."
pipx uninstall assistant-bot

echo "Uninstallation complete."
read -p "Press any key to continue..."
