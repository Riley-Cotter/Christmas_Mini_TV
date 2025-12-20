#!/bin/bash

sudo apt -y update
sudo apt -y upgrade
sudo apt install -y python3-pip
sudo apt-get install -y vlc
sudo sed -i 's/geteuid/getppid/' /usr/bin/vlc
sudo apt-get install -y fbi
sudo apt install -y python3-vlc

#Set shell scripts code to executable
chmod +x /home/ri/Christmas_Mini_TV/*.sh

echo "[✔] Setup Complete"
