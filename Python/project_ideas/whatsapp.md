- Setup
$ pip install pywhatkit

- Script

import pywhatkit as msg

PHONE_NUMBER = "+420773457851"
MESSAGE_TO_SEND = "Hey you!"
HOUR_TO_BE_SENT = 13
MINUTE_TO_BE_SENT = 05

msg.sendwhatmsg(PHONE_NUMBER, MESSAGE_TO_SEND, HOUR_TO_BE_SENT, MINUTE_TO_BE_SENT)