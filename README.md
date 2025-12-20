# Pi_Video_CRT_Player
Plays videos from a pi on a CRT TV


For Windows:
	Download Ubuntu (Windows Subsystem for Linux)

For Mac:
  Just use the Terminal

		
Raspberry Pi Setup:
1. Install Lite OS (using the raspberry pi imager) Warning* 32 bit!
    
2. Include WIFI 
		Username: LocalWIFIUsername
   	Password: #LocalPassword
   	Enable SSH
    
3. ssh into your RaspberryPi and Clone Repository
  
		sudo apt install git -y
  	then
	
		git clone https://github.com/Riley-Cotter/Pi_Video_CRT_Player.git
	
4. Add Program to Startup
  
   		sudo crontab -e

   add
   
   		@reboot /bin/sleep 1; /home/ri/Pi_Video_CRT_Player/startup.sh > /home/ri/mycronlog.txt 2>&1

6. Give Scripts Permission to be Executable

   		sudo chmod +x /home/ri/Pi_Video_CRT_Player/setup.sh
7. Run Setup

		sudo ./Pi_Video_CRT_Player/setup.sh

8. Reboot

		sudo reboot
