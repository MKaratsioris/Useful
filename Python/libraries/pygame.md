- Install
$ pip install pygame

- use in script
from pygame import mixer

music_file = "<path-to-file>.mp3"
mixer.init()
mixer.music.load(music_file)
mixer.music.play()