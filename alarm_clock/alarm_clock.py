# ---------------------------------
# Alarm Clock Project
# ---------------------------------

import time
from datetime import datetime
import pygame

print("===== ALARM CLOCK =====")

# Initialize pygame
pygame.init()

# Alarm Time Input
alarm_time = input("Set Alarm Time (HH:MM:SS): ")

print(f"Alarm Set For {alarm_time}")

while True:

    # Current Time
    current_time = datetime.now().strftime("%H:%M:%S")

    print(current_time, end="\r")

    # Check Alarm
    if current_time == alarm_time:

        print("\n⏰ WAKE UP!")

        # Play Alarm Sound
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        break

    time.sleep(1)
