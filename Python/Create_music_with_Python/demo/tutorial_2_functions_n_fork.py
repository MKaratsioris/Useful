from scamp import Session, wait, current_clock

s = Session()
s.tempo = 100

brass= s.new_part("brass")
def beat_it():
    brass.play_note(40, 1.0, 0.25)
    brass.play_note(43, 1.0, 0.25)
    brass.play_note(47, 1.0, 0.25)
    brass.play_note(55, 1.0, 0.25)
    brass.play_note(52, 1.0, 0.75)
    brass.play_note(54, 1.0, 0.5)
    brass.play_note(52, 1.0, 0.25)
    brass.play_note(50, 1.0, 0.25)
    wait(0.25)
    brass.play_note(50, 1.0, 0.25)
    wait(0.75)

trumpet = s.new_part("trumpet")
def top_part(short_length, medium_length, long_length):
    #current_clock().tempo = 180
    trumpet.play_note(71, 1.0, short_length)
    trumpet.play_note(71, 1.0, long_length)
    trumpet.play_note(71, 1.0, short_length)
    trumpet.play_note(71, 1.0, long_length)
    trumpet.play_note(71, 1.0, medium_length)
    trumpet.play_note(71, 1.0, short_length)
    trumpet.play_note(71, 1.0, short_length)
    trumpet.play_note(71, 1.0, short_length)
    trumpet.play_note(74, 1.0, medium_length)
    trumpet.play_note(71, 1.0, short_length, "staccato")
    trumpet.play_note(74, 1.0, medium_length)
    trumpet.play_note(71, 1.0, short_length, "staccato")

#s.fork(beat_it)
#top_part()

s.fork(top_part, args=[0.25, 0.5, 1.5])
s.fork(beat_it)
#s.wait_forever()  # never exits
s.wait_for_children_to_finish()
