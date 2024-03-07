#!/bin/bash

red_cross() {
    echo -e "\e[31m❌ $1\e[0m"
}

green_check() {
    echo -e "\e[32m✅ $1\e[0m"
}

check_command() {
    if command -v $1 >/dev/null 2>&1; then
        green_check "$1 is installed."
    else
        red_cross "$1 is not installed. Aborting."
        exit 1
    fi
}

# Check for Python
check_command python

# Check for ngrok
check_command ngrok

# if both checks pass, start the server
if [ $? -eq 0 ]; then
    source .env
    pip install -r requirements.txt
    python app.py
fi
