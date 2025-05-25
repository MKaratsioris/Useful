from tkinter import Tk, Button, Listbox, PhotoImage, Frame, Menu, filedialog, END, ACTIVE, ANCHOR
import pygame



# !
# * ADDED Buttons   : Pause/Unpause
# * ADDED Menu bar  : Add many songs
# ?
# TODO Buttons : Next, Previous
# TODO Menu bar: Remove song, Remove all songs
# TODO Song duration
# TODO Song slider
# TODO Song position slider
# TODO Volume control





# /home/mkar/Desktop/Python/projects/music_player_versions/music/623425__zhr__simple-various-piano-music.mp3
SONG_PATH = "/home/mkar/Desktop/Python/projects/music_player_versions/music/623425__zhr__simple-various-piano-music.mp3"

TITLE = "Music Player v2.1"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 325
#ICON = "images/icon.ico"
MUSIC_FOLDER = "/home/mkar/Desktop/Python/projects/music_player_versions/music"
global paused, playing
paused = False
playing = False

root = Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
STARTING_X = SCREEN_WIDTH // 2 - WINDOW_WIDTH // 2
STARTING_Y = SCREEN_HEIGHT // 2 - WINDOW_HEIGHT // 2
GEOMETRY = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{STARTING_X}+{STARTING_Y}"

root.title(TITLE)

root.geometry(GEOMETRY)
root.resizable(0, 0)
#root.iconbitmap(ICON)

pygame.mixer.init()

# Control Buttons Functionality
def add_song() -> None:
    song = filedialog.askopenfilename(initialdir=MUSIC_FOLDER, title='Choose a song', filetypes=(("mp3 Files", "*.mp3"),))
    song = song.replace(MUSIC_FOLDER, "").replace(".mp3", "")

    song_box.insert(END, song)

def add_many_songs() -> None:
    songs = filedialog.askopenfilenames(initialdir=MUSIC_FOLDER, title='Choose a song', filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace(MUSIC_FOLDER, "").replace(".mp3", "")
        song_box.insert(END, song)

def previous_song() -> None:
    pass

def next_song() -> None:
    pass

def play(is_playing: bool) -> None:
    global paused, playing
    playing = is_playing
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    elif not playing:
        song = song_box.get(ACTIVE)
        song = f"{MUSIC_FOLDER}{song}.mp3"
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        playing = True

def pause(is_paused: bool) -> None:
    global paused
    paused = is_paused
    
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def stop() -> None:
    global paused, playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    playing = False
    paused = False

# Playlist of songs
song_box = Listbox(root, bg="black", fg="green", width=100, selectbackground="green", selectforeground="black")
song_box.pack(pady=20)

# Control Button Images
back_btn_img = PhotoImage(file="images/back50.png")
forward_btn_img = PhotoImage(file="images/forward50.png")
play_btn_img = PhotoImage(file="images/play50.png")
pause_btn_img = PhotoImage(file="images/pause50.png")
stop_btn_img = PhotoImage(file="images/stop50.png")

# Control Frame
control_frame = Frame(root)
control_frame.pack()

# Control Buttons
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_btn = Button(control_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=lambda: play(playing))
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
play_btn.grid(row=0, column=1, padx=10)
pause_btn.grid(row=0, column=2, padx=10)
stop_btn.grid(row=0, column=3, padx=10)
forward_btn.grid(row=0, column=4, padx=10)

# Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add 'Add Song' to the menu
add_song_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Add", menu=add_song_menu)
add_song_menu.add_command(label="One", command=add_song)
add_song_menu.add_command(label="PARTY!", command=add_many_songs)



root.mainloop()