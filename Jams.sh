#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

cd "$SCRIPT_DIR/JourneyJams" || { echo "Failed to change directory"; exit 1; }

python downloader.py
