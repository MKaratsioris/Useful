- Setup
$ pip install SpeechRecognition
$ pip install pyaudio

- Script
import speech_recognition as SR

record = SR.Recognizer()
with SR.Microphone() as source:
    print("Hey you!")
    audio = record.listen(source)

print(record.recognize_google(audio))