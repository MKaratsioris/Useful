- Setup
$ pip install pyqrcode png pypng

- Script
import pyqrcode
import png
from pyqrcode import QRCode

input_link = "www.google.com"
qr_code = pyqrcode.create(input_link)

output_file = "<path-to-file>.png"
qr_code.png(output_file, scale=6)