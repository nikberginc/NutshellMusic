import pygame
from pathlib import Path
import tkinter as tk
from PIL import Image, ImageTk
import random
import time
pygame.mixer.init()
import os
import math
songs_folder = Path.home() / "Documents" / "NutshellMusic" / "Songs"
music_files = []
random_played = []
history = []
pygame.mixer.music.set_volume(0.5)
is_paused = False
random_mp3 = False # a button that will be added to GUI



#when button is presed the random will be enabled/set to True
def enable_random(random_checkbox_disable, random_checkbox_enable):
    global random_mp3
    random_mp3 = True

    random_checkbox_disable.place_forget()
    random_checkbox_enable.place(x=620, y=450) 

#when button is presed the random will be disabled/set to False
def disable_random(random_checkbox_enable, random_checkbox_disable):
    global random_mp3
    random_mp3 = False

    random_checkbox_enable.place_forget()
    random_checkbox_disable.place(x=620, y=450) 












#gets curent index for def play_and_select
def get_current_index():
    global current_index
    try:
        return current_index
    except NameError:
        return -1  # means "no song currently playing"







#play music function when user clicks on the song in the list
def play_mp3(music_to_play: Path, unpause_button, pause_button):
    global current_index, history, random_played, is_paused
    history.clear()
    random_played.clear()

    #code will load the music and then play it
    pygame.mixer.music.load(str(music_to_play))
    pygame.mixer.music.play()

    #will store the current index so the next button can work
    current_index = music_files.index(music_to_play)

    #when first song plays and the photo is unpause it will swich to pause
    unpause_button.place_forget()
    pause_button.place(x=470, y=430) 
    is_paused = False









#pause the music whe the button will be pressed
def pause_mp3(pause_button, unpause_button):
    global is_paused
    
    #code will pause the music
    pygame.mixer.music.pause()
    pause_button.place_forget()
    unpause_button.place(x=470, y=430)
    is_paused = True






#play/unpuase  the music after it has been paused
def unpause_mp3(unpause_button, pause_button):
    global is_paused

    #unpause the music whe the button will be pressed again
    pygame.mixer.music.unpause()
    unpause_button.place_forget()
    pause_button.place(x=470, y=430) 
    is_paused = False











#it will play the next sound NEEDS TO HAVE GET_MUSIC_FILES BEFORE ITSELF
def next_mp3(unpause_button, pause_button):
    global current_index, music_files, history

    #if nothing is selected the get_curent_index() will have -1
    idx = get_current_index()
    if idx == -1:  # means nothing is selected
        return  # do nothing safely
    
    #stops the curent music
    pygame.mixer.music.stop()
    history.append(current_index)

    if random_mp3:
        global random_played

        #will store curent song as used one
    
        if current_index not in random_played:
            random_played.append(current_index)


        #if user has just one song it will play just that one
        if len(music_files) == 1:
            random_index = 0
        else:

            # pick a random index different from the current one and store it in to the random_played so it doesnt repete
            available_indexes = [i for i in range(len(music_files)) if i not in random_played]

        
            #checks if all the songs where used
            if not available_indexes:
                random_played.clear()
                available_indexes = list(range(len(music_files)))


            random_index = random.choice(available_indexes)


        current_index = random_index
        next_song = music_files[random_index]

    else:
        random_played.clear()

        #will go to the next song and it it was the last one it will loop again
        current_index = (current_index + 1) % len(music_files)
        next_song = music_files[current_index]

    #play the next song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()


    #if unpause button is selected when next button is click it will replace it with pause photo
    unpause_button.place_forget()
    pause_button.place(x=470, y=430) 


    return current_index








#creates a list of all songs in the Songs folder
def get_music_files():
    global music_files
    if songs_folder.exists():
        music_files = [songs_folder / f for f in os.listdir(songs_folder) if f.lower().endswith(".mp3")]
        music_files.sort()
        return music_files
    return[]





#will get you the previus song, most of the song storing code is in next_mp3 or play_mp3
def previous_mp3(unpause_button, pause_button):
    global current_index

    # makes sure there is something to go back to
    if history:
        current_index = history.pop()
        pygame.mixer.music.load(music_files[current_index])
        pygame.mixer.music.play()


        #if unpause button is selected when previous button is click it will replace it with pause photo
        unpause_button.place_forget()
        pause_button.place(x=470, y=430) 







#volium will increase by 10
def vol_up():
    vol_check = pygame.mixer.music.get_volume()

    if vol_check < 1.0:
        pygame.mixer.music.set_volume(round (vol_check + 0.1 , 1) )
        vol_number()


#volume will decrease by 10
def vol_down():
    vol_check = pygame.mixer.music.get_volume()

    if vol_check > 0.0:
        pygame.mixer.music.set_volume(round (vol_check - 0.1 , 1) )
        vol_number()



def vol_number():
    #will return to GUI user freandy number (from 0.3 to 30)
    return f"{math.ceil(pygame.mixer.music.get_volume() * 100)}%"




#we dont need this
#get_music_files()
#
#
#play_mp3(music_to_play)
#time.sleep(1)
#current_volume = pygame.mixer.music.get_volume()
#print(current_volume)

#while True:



#    x = input()
#    if x == "e":
#        next_mp3()
#
#    elif x == "c":
#        break
#    elif x == "true":
#        random_mp3 = True
#   elif x == "false":
#         random_mp3 = False
#    elif x == "pause":
#        pause_mp3()
#    elif x == "play":
#        unpause_mp3()
#    elif x == "back":
#       previous_mp3()
#    elif x == "up":
#        vol_up()
#        print(vol_number)
#    elif x == "down":
#        vol_down()
#        print(vol_number)

