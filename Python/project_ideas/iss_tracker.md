- Setup
$ pip install requests
$ pip install jsonlib
$ pip install turtle
$ pip install urllib3
$ pip install times

- Script
import json
import turtle
import urllib.request
import time
import webbrowser

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

# -------------------------------

location = result["iss_position"]
latitude = float(location['latitude'])
longitute = float(location['longitude'])

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

