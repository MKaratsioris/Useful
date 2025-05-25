import csv

from music.Scale import Scale
from instruments.Piano import Piano
from music.MelodyLine import MelodyLine

file_name = "partituras/scales/c4_major.csv"
tempo = 120

piano = Piano(tempo=tempo)

MELODY = MelodyLine()


with open(file_name, "r") as melody_file:
    melody_notes = csv.reader(melody_file)
    for row in melody_notes:
        note, volume, duration = row
        if note != 'note':
            MELODY.add_note(note, float(volume), float(duration))

piano.play_melody(MELODY)