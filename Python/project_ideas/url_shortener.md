- Setup
$ pip install pyshorteners

- Script
import pyshorteners as psn

url = "https://www.google.com"
short_url = psn.Shortener().tinyurl.short(url)

print(short_url)