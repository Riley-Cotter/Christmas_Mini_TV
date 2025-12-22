#!/bin/bash

SOURCE="/media/usb"
DEST="/home/ri/videos"

# Create destination directory if it doesn't exist
sudo mkdir -p "$DEST"

# Sync source to destination (mirror)
sudo rsync -av --delete "$SOURCE" "$DEST"
