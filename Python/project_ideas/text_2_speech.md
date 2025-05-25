- Setup
$ pip install playsound
$ pip install gtts  # Google Text To Speech

- Script
import gtts
from playsound import playsound

tts = gtts.gTTS("Hey you!")
tts.save("hey_you.mp3")
