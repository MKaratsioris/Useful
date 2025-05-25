from tkinter import Tk, Listbox, PhotoImage, Frame, Button, Menu, filedialog, END
import pygame
import os

#from music_player_utils import *

TITLE = "Music Player v1.0"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 325

window = Tk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
STARTING_X = SCREEN_WIDTH // 4 - WINDOW_WIDTH // 2
STARTING_Y = SCREEN_HEIGHT // 2 - WINDOW_HEIGHT // 2
GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{STARTING_X}+{STARTING_Y}"

window.title(TITLE)
window.geometry(GEOMETRY)
window.resizable(0, 0)

pygame.mixer.init()

# Main functions#
songs = []
current_song = ""
paused = False
def load_music():
    global current_song
    window.directory = filedialog.askdirectory()
    
    for song in os.listdir(window.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
            
    for song in songs:
        songs_list.insert("end", song)
    
    songs_list.selection_set(0)
    current_song = songs[songs_list.curselection()[0]]



def play_song():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False



def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

        
def next_song():
    global current_song, paused
    
    try:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(songs.index(current_song)+1)
        current_song = songs[songs_list.curselection()[0]]
        play_song()
    except :
        pass
    


def previous_song():
    global current_song, paused
    
    try:
        songs_list.selection_clear(0, END)
        songs_list.selection_set(songs.index(current_song)-1)
        current_song = songs[songs_list.curselection()[0]]
        play_song()
    except:
        pass
        

# Menubar
menu_bar = Menu(window) 
window.config(menu=menu_bar)  # Create a menu bar
organized_menu = Menu(menu_bar, tearoff=False)  # Create a submenu
organized_menu.add_command(label="Add music", command=load_music)  # Add the command 'Add music' to the submenu
menu_bar.add_cascade(label="My Music", menu=organized_menu)  # Add a submenu 'My Music' to the menu bar with the command 'Add music'

# Main window where the songs will be displayed
songs_list = Listbox(window, bg="black", fg="white", width=100, height=15)
songs_list.pack()

# Control lower frame
control_frame = Frame(window)
control_frame.pack()

play_btn_img = PhotoImage(file="images/play.png")
pause_btn_img = PhotoImage(file="images/pause.png")
next_btn_img = PhotoImage(file="images/next.png")
previous_btn_img = PhotoImage(file="images/previous.png")


play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_song)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_song)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_song)
previous_btn = Button(control_frame, image=previous_btn_img, borderwidth=0, command=previous_song)

previous_btn.grid(row=0, column=0, padx=7, pady=10)
play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)

window.mainloop()

