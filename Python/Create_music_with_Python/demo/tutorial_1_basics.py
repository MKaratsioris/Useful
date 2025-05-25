from scamp import Session, Envelope

tempo = 100

#s = Session()
#s.tempo = tempo

s = Session(tempo=tempo)
#s.print_default_soundfont_presets()
# Preset[000:071] Clarinet 2 bag(s) from #80


clarinet = s.new_part("clarinet")
oboe = s.new_part("oboe")
bandoneon = s.new_part("bandoneon")
accordeon = s.new_part("accordeon")

midi_pitch_value = 70  # middle C
volume = 0.8  # 0.0 to 1.0
duration = 0.5  # in seconds


pitches = [60, 64, 66, 69, 67, 64, 60, 57, 54, 54, 54, 55]
rhythms = [1.5, 1.0, 1.0, 0.5, 1.5, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5]
"""
#oboe.play_note(84, 0.8, 10.0, blocking=False)  # Plays in parallel with clarinet
oboe.play_note(84, 0.8, 10.0, blocking=True)  # Plays first, then the clarinet

for pitch, rhythm in zip(pitches, rhythms):
    clarinet.play_note(pitch, 0.8, rhythm)


for pitch, rhythm in zip(pitches, rhythms):
    clarinet.play_note(pitch, 0.8, rhythm, "staccato")
    #clarinet.play_note(pitch, 0.8, rhythm, "param_vibrato: 5")

for pitch, rhythm in zip(pitches, rhythms):
    clarinet.play_note(pitch, 0.8, rhythm, "#")
#    clarinet.play_note(pitch, 0.8, rhythm, "key: Bb")
"""
#clarinet.play_chord([76, 79, 84], 0.8, 5.0)

#for pitch, rhythm in zip(pitches, rhythms):
#    bandoneon.play_note(pitch, 0.8, rhythm)

#bandoneon.play_note([76, 79, 70, 84], 0.8, 5.0)  # glissando solo
#bandoneon.play_chord([76, 79, 70, 84], [0.8, 0.3, 0.2, 1.0], 5.0)

#for pitch, rhythm in zip(pitches, rhythms):
#    accordeon.play_note(pitch, 0.8, rhythm)

#forte_piano_crescendo = Envelope.from_levels_and_durations([0.8, 0.2, 1.0], [0.1, 0.9])
forte_piano_crescendo = Envelope.from_levels_and_durations([0.8, 0.2, 1.0], [0.1, 0.9], [-5, 5])
forte_piano_crescendo.show_plot()

bandoneon.play_chord([76, 79, 70, 84], forte_piano_crescendo, 5.0)