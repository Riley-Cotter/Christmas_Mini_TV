#!/bin/bash

LOG_FILE="/home/ri/mycronlog.txt"
echo -e "\n== Startup initiated: $(date) ==" > "$LOG_FILE"

# Mount USB
echo -e "Start USB MOUNT" >> "$LOG_FILE"
/home/ri/Christmas_Mini_TV/mount_usb.sh >> "$LOG_FILE" 2>&1 &

# Pull latest repo update
/bin/sleep 5
echo -e "Pull Repo" >> "$LOG_FILE"
/home/ri/Christmas_Mini_TV/pull_repo.sh >> "$LOG_FILE" 2>&1 

# Start video player
/bin/sleep 5
echo -e "Start Video Player" >> "$LOG_FILE"
#/usr/bin/python3 /home/ri/Christmas_Mini_TV/video_player.py >> "$LOG_FILE" 2>&1 &

# Optional: keep script alive to prevent service from exiting (if needed)
wait
