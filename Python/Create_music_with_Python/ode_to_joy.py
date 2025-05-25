import csv
from scamp import Session, wait_for_children_to_finish

from utils.constants import NOTE_2_MIDI

s = Session(tempo=140)
piano = s.new_part("piano")
violin = s.new_part("violin")
cello = s.new_part("cello")

print(f"{s.instrument_}")

ode_to_joy_melody_file = "partituras/ode_to_joy/ode_to_joy_melody_1_17.csv"
ode_to_joy_bass_file = "partituras/ode_to_joy/ode_to_joy_bass_1_17.csv"
piano_ode_to_joy_notes_melody = []
piano_ode_to_joy_volumes_melody = []
piano_ode_to_joy_durations_melody = []
piano_ode_to_joy_notes_bass = []
piano_ode_to_joy_volumes_bass = []
piano_ode_to_joy_durations_bass = []

violin_ode_to_joy_notes_melody = []
violin_ode_to_joy_volumes_melody = []
violin_ode_to_joy_durations_melody = []

cello_ode_to_joy_notes_bass = []
cello_ode_to_joy_volumes_bass = []
cello_ode_to_joy_durations_bass = []

def ode_to_joy_violin_melody():
    with open(ode_to_joy_melody_file, "r") as melody_file:
        melody_notes = csv.reader(melody_file)
        for i, row in enumerate(melody_notes):
            if i != 0:
                note, volume, duration = row
                violin_ode_to_joy_notes_melody.append(note)
                violin_ode_to_joy_volumes_melody.append(float(volume))
                violin_ode_to_joy_durations_melody.append(float(duration))            

    for i in range(len(violin_ode_to_joy_notes_melody)):
        note = violin_ode_to_joy_notes_melody[i]
        midi = NOTE_2_MIDI[note]
        volume = violin_ode_to_joy_volumes_melody[i] * 0.6
        duration = violin_ode_to_joy_durations_melody[i]
        print(F"{i + 1}.\t{note}")
        violin.play_note(midi, volume, duration)

def ode_to_joy_cello_bass():
    with open(ode_to_joy_bass_file, "r") as bass_file:
        bass_notes = csv.reader(bass_file)
        for i, row in enumerate(bass_notes):
            if i != 0:
                note_root, note_third, note_fifth, volume, duration = row
                cello_ode_to_joy_notes_bass.append([note_root, note_third, note_fifth])
                cello_ode_to_joy_volumes_bass.append(float(volume))
                cello_ode_to_joy_durations_bass.append(float(duration))            

    for i in range(len(cello_ode_to_joy_notes_bass)):
        root, third, fifth = cello_ode_to_joy_notes_bass[i]
        if root != "0":
            midi_root = NOTE_2_MIDI[root]
            midi_third = NOTE_2_MIDI[third]
            midi_fifth = NOTE_2_MIDI[fifth]
            volume = cello_ode_to_joy_volumes_bass[i] * 0.8
            duration = cello_ode_to_joy_durations_bass[i]
            print(F"  \t{root}-{third}-{fifth}")
            cello.play_chord([midi_root, midi_third, midi_fifth], volume, duration)

def ode_to_joy_piano_melody():
    with open(ode_to_joy_melody_file, "r") as melody_file:
        melody_notes = csv.reader(melody_file)
        for i, row in enumerate(melody_notes):
            if i != 0:
                note, volume, duration = row
                piano_ode_to_joy_notes_melody.append(note)
                piano_ode_to_joy_volumes_melody.append(float(volume))
                piano_ode_to_joy_durations_melody.append(float(duration))            

    for i in range(len(piano_ode_to_joy_notes_melody)):
        note = piano_ode_to_joy_notes_melody[i]
        midi = NOTE_2_MIDI[note]
        volume = piano_ode_to_joy_volumes_melody[i]
        duration = piano_ode_to_joy_durations_melody[i]
        print(F"\t{note}")
        piano.play_note(midi, volume, duration)

def ode_to_joy_piano_bass():
    with open(ode_to_joy_bass_file, "r") as bass_file:
        bass_notes = csv.reader(bass_file)
        for i, row in enumerate(bass_notes):
            if i != 0:
                note_root, note_third, note_fifth, volume, duration = row
                piano_ode_to_joy_notes_bass.append([note_root, note_third, note_fifth])
                piano_ode_to_joy_volumes_bass.append(float(volume))
                piano_ode_to_joy_durations_bass.append(float(duration))            

    for i in range(len(piano_ode_to_joy_notes_bass)):
        root, third, fifth = piano_ode_to_joy_notes_bass[i]
        if root != "0":
            midi_root = NOTE_2_MIDI[root]
            midi_third = NOTE_2_MIDI[third]
            midi_fifth = NOTE_2_MIDI[fifth]
            volume = piano_ode_to_joy_volumes_bass[i] * 0.8
            duration = piano_ode_to_joy_durations_bass[i]
            print(F"\t{root}-{third}-{fifth}")
            piano.play_chord([midi_root, midi_third, midi_fifth], volume, duration)

#s.fork(ode_to_joy_violin_melody)
#s.fork(ode_to_joy_piano_melody)
#s.fork(ode_to_joy_piano_bass)
#s.fork(ode_to_joy_cello_bass)
#wait_for_children_to_finish()
