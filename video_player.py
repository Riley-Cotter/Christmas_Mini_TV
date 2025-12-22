import os
import vlc
import time
import RPi.GPIO as GPIO

# ---------------- GPIO SETUP ----------------
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 26
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# ---------------- VLC SETUP ----------------
VIDEO_DIR = "/home/ri/videos/usb"
VIDEO_EXT = (".mp4", ".mkv", ".avi", ".mov")

instance = vlc.Instance("--aout=alsa")
player = None   # Global player reference


# ---------------- BUTTON CALLBACK ----------------
def button_callback(channel):
    global player
    if player is not None:
        print("Button pressed → stopping video")
        player.stop()


# Register button interrupt ONCE
GPIO.add_event_detect(
    BUTTON_PIN,
    GPIO.FALLING,
    callback=button_callback,
    bouncetime=300
)

# ---------------- MAIN LOOP ----------------
try:
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
            player.play()

            # Wait for playback to actually start
            start_timeout = time.time() + 5
            while player.get_state() in (
                vlc.State.NothingSpecial,
                vlc.State.Opening
            ):
                if time.time() > start_timeout:
                    print("⚠️ VLC failed to start playback.")
                    break
                time.sleep(0.1)

            # Monitor playback
            while True:
                state = player.get_state()
                if state in (
                    vlc.State.Ended,
                    vlc.State.Stopped,
                    vlc.State.Error
                ):
                    break
                time.sleep(0.3)

            player.stop()
            time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()
