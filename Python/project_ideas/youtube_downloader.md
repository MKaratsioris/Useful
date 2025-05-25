- Setup
$ pip install pytube

- Script
from pytube import YouTube

youtube_link = "https://www.youtube.com/watch?v=amHRwUEkCYQ"
video = YouTube(youtube_link)
stream = video.streams.get_highest_resolution()
stream.download()