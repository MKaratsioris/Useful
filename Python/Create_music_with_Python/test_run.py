"""
from pathlib import Path

_current_directory = Path(__file__).parent.resolve()

print(_current_directory)
"""
# -------------------------------------------

from scamp import Session
from music.Partitura import Partitura

tempo = 100
instruments = ["piano", "violin"]
piano_melody = "partituras/scales/c4_major_melody.csv"

music = Partitura(tempo=tempo, instruments=instruments)
#music.play_instrument("violin", piano_melody)
music.play_partitura()