from tkinter import Tk, Button
import pygame



# !
# * Installed and explored basic functionality of tkinter and pygame for sound
# ?
# TODO





# /home/mkar/Desktop/Python/projects/music_player_versions/music/623425__zhr__simple-various-piano-music.mp3
SONG_PATH = "/home/mkar/Desktop/Python/projects/music_player_versions/music/623425__zhr__simple-various-piano-music.mp3"

TITLE = "Music Player v2.0"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 325
#ICON = "images/icon.ico"

root = Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
STARTING_X = SCREEN_WIDTH // 4 - WINDOW_WIDTH // 2
STARTING_Y = SCREEN_HEIGHT // 2 - WINDOW_HEIGHT // 2
GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{STARTING_X}+{STARTING_Y}"

root.title(TITLE)
root.geometry(GEOMETRY)
root.resizable(0, 0)
#root.iconbitmap(ICON)

pygame.mixer.init()

def play():
    pygame.mixer.music.load(SONG_PATH)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

play_button = Button(root, text="Play", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 32), command=stop)
stop_button.pack(pady=20)

root.mainloop()