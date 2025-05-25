from scamp import Session, wait
import random

TITLE = "First Composition"
COMPOSER = "DJ Greco"
TIME_SIGNATURE ="2/4"
BAR_LINE_LOCATIONS = [4, 7, 9.5, 12, 17, 20]
MAX_DIVISOR = 4

s = Session(default_spelling_policy="Bb minor")

s.fast_forward_to_beat(1_000)

clarinet = s.new_part("clarinet")
bassoon = s.new_part("bassoon")

bass_notes = [58, 57, 56, 55, 54, 51, 53, 41] * 2 + [46, 47, 48, 49, 50, 53, 56, 55, 52, 53]
clarinet_patterns = [[20, 15, 20], [None, 12, 14, 15], [None, 15, 9, 12], [19, 17, 16], [16]]

def bassoon_part():
    for bass_note in bass_notes:
#        bassoon.play_note(bass_note, 1.0, 1.0, "spelling: Bb minor")
#        bassoon.play_note(bass_note, 1.0, 1.0, "spelling: #")
#        bassoon.play_note(bass_note, 1.0, 1.0, "#")
#        bassoon.play_note(bass_note, 1.0, 1.0, "spelling: b")
#        bassoon.play_note(bass_note, 1.0, 1.0, "staccato")
        bassoon.play_note(bass_note, 1.0, 1.0)

def clarinet_part():
    for bass_note in bass_notes:
        pattern = random.choice(clarinet_patterns)
        note_length = 1 / len(pattern)
        for interval in pattern:
            if interval is None:
                wait(note_length)
            else:
                clarinet.play_note(bass_note + interval, 1.0, note_length)

s.start_transcribing()
s.fork(clarinet_part)
s.fork(bassoon_part)
s.wait_for_children_to_finish()
transcription = s.stop_transcribing()
#print(transcription)
transcription.to_score(
    title=TITLE,
    composer=COMPOSER,
    max_divisor=MAX_DIVISOR,
    time_signature=TIME_SIGNATURE
    ).show()  # .show_xml() # use that to produce a file to produce with Musescore