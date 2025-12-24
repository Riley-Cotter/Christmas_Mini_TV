
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

3. While sd card is still in computer, follow instructions here (adding dtoverlays to config and overlay file): https://www.waveshare.com/wiki/2.8inch_DPI_LCD
    
5. ssh into your RaspberryPi and Clone Repository
  
		sudo apt install git -y
  	then
	
		git clone https://github.com/Riley-Cotter/Christmas_Mini_TV.git
	
6. Add Program to Startup
  
   		sudo crontab -e

   add

       @reboot /bin/sleep 1; /home/ri/Christmas_Mini_TV/startup.sh > /home/ri/mycronlog.txt 2>&1

7. Give Scripts Permission to be Executable

   		sudo chmod +x /home/ri/Christmas_Mini_TV/setup.sh

8. Run Setup

		sudo ./Christmas_Mini_TV/setup.sh

9. Copy over videos

    	sudo ./Christmas_Mini_TV/copy_usb_to_sd.sh
