#!/bin/bash

SOURCE="/media/usb/"
DEST="/videos/"

# Create destination directory if it doesn't exist
mkdir -p "$DEST"

# Sync source to destination (mirror)
rsync -av --delete "$SOURCE" "$DEST"
