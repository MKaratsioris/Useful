- Setup
$ pip install googletrans=3.1.0a0

- Script
import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)
translator = Translator()

phrase = "I know that I do not know"
translation = translator.translate(phrase, dest='el')
print(translation)