import os
import vlc
import time
import RPi.GPIO as GPIO

# Use the BCM pin numbering scheme (GPIO numbers, not physical pin numbers)
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin the button is connected to
BUTTON_PIN = 26

# Set up the button pin as an input, and enable the internal pull-up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Videos location and types:
VIDEO_DIR = "/home/ri/videos/usb"
VIDEO_EXT = (".mp4", ".mkv", ".avi", ".mov")

# Create Video Instance
instance = vlc.Instance("--aout=alsa")

#Create Volume Level 
VolLevel = 100

while True:
    files = sorted([
        os.path.join(VIDEO_DIR, f)
        for f in os.listdir(VIDEO_DIR)
        if f.lower().endswith(VIDEO_EXT)
    ])
    
    for video in files:
        print(f"Playing: {video}")

        player = instance.media_player_new()
        media = instance.media_new(video)
        player.set_media(media)

        player.video_set_aspect_ratio("3:4")
        player.audio_set_volume(VolLevel)
        player.play()
        
        # --- WAIT UNTIL PLAYBACK ACTUALLY STARTS ---
        start_timeout = time.time() + 5  # max 5 seconds
        while player.get_state() in (vlc.State.NothingSpecial, vlc.State.Opening):
            if time.time() > start_timeout:
                print("⚠️ VLC failed to start playback.")
                break
            time.sleep(0.1)

        # --- MONITOR UNTIL VIDEO ENDS ---
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                count = 0
                time.sleep(.1)
                while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                    time.sleep(0.1)
                    count = count + 0.1
                    if count > 5:
                        player.stop()
                        time.sleep(5.0)
                        while GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                            time.sleep(0.2)
                        
                        break
                if count < 1:
                    if VolLevel == 100:
                        VolLevel = 0
                    else:
                        VolLevel = 100
                    player.audio_set_volume(VolLevel)
                if count > 1 and count < 5:
                    player.stop()
                    break
                
                        
            state = player.get_state()
            if state in (vlc.State.Ended, vlc.State.Error, vlc.State.Stopped):
                break
            time.sleep(0.1)

        # Give VLC time to release the file
        player.stop()
        time.sleep(1)
        
    
