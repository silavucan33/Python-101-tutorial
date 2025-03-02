# Python Alarm Clock

#we'll be updating our clock every second
import time
import datetime #the datetime module allows us to work with string representations of a time

#a way to work with sound effects is use pygame
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "music.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        #we could method chain the string format method
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP! 😫")

            pygame.mixer.init()
        #mixer is a module for loading and playing sounds
        #the initialize method another way to call the constructor (we can pass in some keyword arguments for the frequency; size, channels, buffer)
        #but maybe that might be a little too complicated for us at this level. we'll use the default settings by not passing in anything
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

#our sound file stops playing when the program terminates
#so, to continue playing our sound file while that sound file is busy

            while pygame.mixer.music.get_busy():
                time.sleep(1)

#'get_busy' method returns a boolean. if our song is busy, if it's still playing then we will call the time modules 'sleep' method
#test if any sound is being mixed (pygame mixer method)
#Returns True if the mixer is busy mixing any channels. If the mixer is idle then this return False.

            is_running = False
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


