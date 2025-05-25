import pandas as pd
import json
from CONSTANTS import PIANO_PITCHES_INFO
"""
midi_values_df = pd.read_csv("pitches.csv").iloc[::-1]
midi_values_df = midi_values_df.set_index("piano_key")

pitches: dict[str,dict] = {}
info: dict = {}

with open("pitches.csv", mode='r') as csv_file:
    for piano_key in midi_values_df.index:
        note_name = midi_values_df["note_name"][piano_key]
        midi_tone = int(midi_values_df["midi_tone_number"][piano_key])
        frequency = float(midi_values_df["frequency"][piano_key])
        info["piano_key"] = piano_key
        info["midi_tone"] = midi_tone
        info["frequency"] = frequency
        pitches[note_name] = INFO.copy()

print(json.dumps(
    pitches,
    sort_keys=True,
    indent=4,
    separators=(',', ': ')
))

with open('pitches.json', 'w') as json_file:
    json.dump(PITCHES, json_file)

print(json.dumps(
    PIANO_PITCHES,
    sort_keys=True,
    indent=4,
    separators=(',', ': ')
))
"""