- Install
$ pip install textblob

- Use in script
from textblob import TextBlob

initial_phrase = TextBlob("blablablabla")
corrected_phrase = initial_phrase.correct()

print(corrected_phrase)