from pathlib import Path
import tkinter as tk
import sys
import time
import os
import random
import math
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import pygame
pygame.mixer.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT)
#my programs
from Saving_mp3 import copy_mp3
import Player_functions
from Player_functions import unpause_mp3, pause_mp3, next_mp3, previous_mp3, play_mp3, get_music_files, vol_down, vol_up, get_current_index, enable_random, disable_random, vol_number
#for chacking list of songs
songs_folder = Path.home() / "Documents" / "NutshellMusic" / "Songs"
#will help for get_music_files
music_files = get_music_files()
random_played = []
history = []
current_index = -1
encrypt = False
get_music_files()
pygame.mixer.music.set_volume(0.5)
first = False
     





#needed so the .exe file finds all imiges
def resource_path(relative_path):
    # If running as .exe, sys._MEIPASS is the temp folder where PyInstaller unpacks files
    try:
        base_path = Path(sys._MEIPASS)
    except Exception:
        base_path = Path(__file__).parent
    return base_path / relative_path









def drop(event):
    global encrypt
    # safely split multiple files
    files = window.tk.splitlist(event.data)

    for file in files:
        file_path = Path(file)  # full path to this file

        if file_path.suffix.lower() != ".mp3":
            continue  # skip non-MP3 files


        copy_mp3(file_path, encrypt.get(), file_path.stem)

    # refresh listbox so new songs appear
    refresh_listbox()







#refreshesh volume number
def refresh_volume():
    volume_label.config(text=vol_number())






#will set volume up and update volume number
def vol_up_and_update():
    vol_up()
    refresh_volume()






#will set volume up and update volume number
def vol_down_and_update():
    vol_down()    
    refresh_volume()






#it will refresh the listbox
def refresh_listbox():
    global music_files
    # re-scan the folder (this returns a fresh list of Path objects)
    music_files = get_music_files()

    # rebuild the Listbox
    music_listbox.delete(0, tk.END)
    for song_path in music_files:
        music_listbox.insert(tk.END, "")
        music_listbox.insert(tk.END, song_path.stem)

    # keep the highlight on the currently-playing song (if valid)
    idx = get_current_index()
    if 0 <= idx < len(music_files):
        listbox_index = idx * 2 + 1
        music_listbox.selection_clear(0, tk.END)
        music_listbox.selection_set(listbox_index)
        music_listbox.see(listbox_index)
        music_listbox.update_idletasks()









#two functions for play_and_select and next_mp3
def next_and_update():
    Player_functions.next_mp3(unpause_button, pause_button)
    play_and_select()


def previous_and_update():
    Player_functions.previous_mp3(unpause_button, pause_button)
    play_and_select()





#function that will select visualy next song
def play_and_select():
    current_index = get_current_index()
    if current_index >= 0 and current_index < len(music_files):
        listbox_index = current_index * 2 + 1  # correct for blank lines
        music_listbox.selection_clear(0, tk.END)
        music_listbox.selection_set(listbox_index)
        music_listbox.see(listbox_index)
        music_listbox.update_idletasks()













#customizing window
window = TkinterDnD.Tk()
window.title("NutshellMusic")
window.geometry("1000x550")
window.configure(bg="#AC937C")
window.resizable (False, False)



icon_path = resource_path("NutshellMusic_icon.ico")
window.iconbitmap(str(icon_path))




#check box helper to set encrypt to False or true
encrypt = tk.BooleanVar(value=False)






#photo, comand, for UNPAUSE button
img_path = resource_path("unpause_button_photo.png")
img = Image.open(img_path)
img = img.resize((60, 60))
unpause_photo = ImageTk.PhotoImage(img)

unpause_button = tk.Button(window, text="▶ Play", image = unpause_photo, command=unpause_mp3, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
unpause_button.config(command=lambda: Player_functions.unpause_mp3(unpause_button, pause_button))

















#photo, comand, posision for PAUSE button
img_path = resource_path("pause_button_photo.png")
img = Image.open(img_path)
img = img.resize((60, 60))
pause_photo = ImageTk.PhotoImage(img)


pause_button = tk.Button(window, text="▶ Pause", image=pause_photo, command=pause_mp3, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")

pause_button.config(command=lambda: Player_functions.pause_mp3(pause_button, unpause_button))
pause_button.place(x = 470, y = 430)















#photo, command, posision for NEXT button
img_path = resource_path("next_button_photo.png")
img = Image.open(img_path)
img = img.resize((50, 50))
next_photo = ImageTk.PhotoImage(img)


next_button = tk.Button(window, text="▶▶I Next", image=next_photo, command=next_and_update, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
next_button.place(x = 550, y = 440)













#photo, command, posision for PREVIOUS button
img_path = resource_path("previous_button_photo.png")
img = Image.open(img_path)
img = img.resize((50, 50))
previous_photo = ImageTk.PhotoImage(img)

previous_button = tk.Button(window, text="I◀◀ Previous", image=previous_photo, command=previous_and_update, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
previous_button.place(x = 400, y = 440)















#photo, command, posision for REFRESH button
img_path = resource_path("refresh_button_photo.png")
img = Image.open(img_path)
img = img.resize((50, 50))
refresh_photo = ImageTk.PhotoImage(img)


refresh_button = tk.Button(window, text="Reload",  image=refresh_photo, command=refresh_listbox, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
refresh_button.place(x = 870, y = 40)



#add on for REFRESH button, a simple LINE
img_path = resource_path("line_refresh_label_photo.png")
img = Image.open(img_path)
img = img.resize((30, 20))
line_photo = ImageTk.PhotoImage(img)


line_label = tk.Label(window, text="Line",  image=line_photo, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
line_label.place(x = 840, y = 55)
















#add on for RANDOM button, a disabled RANDOM checkbox         (this one enables the random but has icon to disable)
img_path = resource_path("random_button_photo_disabled.png")
img = Image.open(img_path)
img = img.resize((30, 30))
random_photo_disable = ImageTk.PhotoImage(img)


random_checkbox_disable = tk.Button(window, text="Random off",  image=random_photo_disable, command=enable_random, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
random_checkbox_disable.config(command=lambda: Player_functions.enable_random(random_checkbox_disable, random_checkbox_enable))

random_checkbox_disable.place(x = 620, y = 450)



#add on for RANDOM button, a enabled RANDOM checkbox           (this one desables random but changes icon to enable)
img_path = resource_path("random_button_photo_enabled.png")
img = Image.open(img_path)
img = img.resize((30, 30))
random_photo_enable = ImageTk.PhotoImage(img)

random_checkbox_enable = tk.Button(window, text="Random on",  image=random_photo_enable, command=disable_random, bd=0, highlightthickness=0, relief="flat", activebackground="#AC937C")
random_checkbox_enable.config(command=lambda: Player_functions.disable_random(random_checkbox_enable, random_checkbox_disable))















#photo, command, posision for VOLUME button

img_path = resource_path("vol_label_photo.png")
img = Image.open(img_path)
img = img.resize((40, 40))
vol_label_photo = ImageTk.PhotoImage(img)


img_path = resource_path("vol_up_photo.png")
img = Image.open(img_path)
img = img.resize((20, 20))
vol_up_photo = ImageTk.PhotoImage(img)

img_path = resource_path("vol_down_photo.png")
img = Image.open(img_path)
img = img.resize((20, 20))
vol_down_photo = ImageTk.PhotoImage(img)

img_path = resource_path("vol_squere_photo.png")
img = Image.open(img_path)
img = img.resize((150, 70))
vol_all_squere_photo = ImageTk.PhotoImage(img)

img_path = resource_path("square_vol_number_photo.png")
img = Image.open(img_path)
img = img.resize((49, 38))
vol_number_squere_photo = ImageTk.PhotoImage(img)





#volume squere
vol_squere = tk.Label(window, image=vol_all_squere_photo, bd=0, highlightthickness=0, relief="flat", activebackground="#5C4033")
vol_squere.place(x = 720, y = 440)




#volume icon
vol_label = tk.Label(window, text="Volume_label" , image=vol_label_photo, bd=0, highlightthickness=0, relief="flat", activebackground="#5C4033")
vol_label.place(x = 735, y = 455)




#volume down
vol_down_button = tk.Button(window, text="Volume_down" , image=vol_down_photo, command=vol_down_and_update, bd=0, highlightthickness=0, relief="flat", activebackground="#5C4033")
vol_down_button.place(x = 780, y = 465)




#volume up
vol_up_button = tk.Button(window, text="Volume_up" , image=vol_up_photo, command=vol_up_and_update, bd=0, highlightthickness=0, relief="flat", activebackground="#5C4033")
vol_up_button.place(x = 820, y = 465)


#background for volume number
vol_number_label = tk.Label(window, image= vol_number_squere_photo, bd=0, highlightthickness=0, relief="flat", activebackground="#E09563")
vol_number_label.place(x=885, y=460)



#user can see the number of a volume thay have (50%)
volume_label = tk.Label(window, text=vol_number(), bg="#AC937C", fg="black", font=("Comic Sans MS", 10, "bold"),)
volume_label.place(x=890, y=465)










img_path = resource_path("drag_and_drop_photo.png")
img = Image.open(img_path)
img = img.resize((170, 220))
drag_and_drop_photo = ImageTk.PhotoImage(img)


drag_drop_label = tk.Label(window, text="DRAG AND DROP .MP3",image=drag_and_drop_photo, bg="#C0C0C0", fg="black", font=("Helvetica", 12, "bold"), width=120, height=220, bd=0, relief="ridge")
drag_drop_label.place(x=50, y=70)










#images for checked and unchecked box
img_path = resource_path("checkbox_False_photo.png")
img = Image.open(img_path)
img = img.resize((20, 20))
checkbox_False_photo = ImageTk.PhotoImage(img)

img_path = resource_path("checkbox_True_photo.png")
img = Image.open(img_path)
img = img.resize((20, 20))
checkbox_True_photo = ImageTk.PhotoImage(img)



#checkbox for encrypting music for drag and drop
checkbox = tk.Checkbutton(
    window,
    variable=encrypt, 
    bg="#cbd5e1", 
    image=checkbox_False_photo, 
    selectimage=checkbox_True_photo, 
    bd=0, 
    highlightthickness=0, 
    relief="flat", 
    activebackground="#cbd5e1", 
    selectcolor="#cbd5e1", 
    indicatoron=False, 
    padx=30, 
    pady=30,
    )
checkbox.place(x =100, y=230)











#LISTBOX window settings
music_listbox = tk.Listbox(window, bg="#B97A57", fg="black", font=("Helvetica", 12, "bold"), width=70, height=15, selectbackground="#E09563")
music_listbox.place(x=200, y=50)

#will sent all MP# files to the listbox
for songs_folder in music_files:
    music_listbox.insert(tk.END, "") 
    music_listbox.insert(tk.END, songs_folder.stem)







#will sent a signal to play_mp3 to play the song
def on_song_select(event):
    global first
    selection = music_listbox.curselection()
    if selection:
        index = selection[0]
        song_name = music_listbox.get(index)
        
        # Skip blank lines
        if song_name.strip() == "":
            return
        
        # Find the Path object for this song
        for song_path in music_files:
            if song_path.stem == song_name:
                first = True
                play_mp3(song_path, unpause_button, pause_button)
                break

# Bind the Listbox selection
music_listbox.bind("<<ListboxSelect>>", on_song_select)






def check_music_end():
    global current_index, first
    # only go to next song if not paused
    if first:
        if not pygame.mixer.music.get_busy() and not Player_functions.is_paused:
            current_index = Player_functions.next_mp3(unpause_button, pause_button)
            play_and_select()
    window.after(500, check_music_end)



#add to for checking if song ends
check_music_end()




drag_drop_label.drop_target_register(DND_FILES)
drag_drop_label.dnd_bind("<<Drop>>", drop)


window.mainloop()