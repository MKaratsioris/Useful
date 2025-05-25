- Setup
$ pip install progressbar

- Script
from time install sleep
from progressbar import ProgressBar

status_bar = ProgressBar()

for _ in status_bar(range(40)):
    sleep(0.1)