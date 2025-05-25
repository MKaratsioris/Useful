from utils.constants import NOTE_2_MIDI, MIDI_2_NOTE, SCALES

class Scale:
    def __init__(self, name: str = "Major", note: str = "C", octave: int = 4) -> None:
        self.octave: int = octave
        self.tonic: str = f"{note}{self.octave}"
        self.name: str = name
        
        self.scale_midi: list[float] = []
        self.scale_notes: list[str] = []
                
        def __build_scale(self, scale_name: str) -> None:
            self.major_steps = SCALES[scale_name]  # list[float]
            self.scale_midi.append(float(NOTE_2_MIDI[self.tonic]))
            self.scale_notes.append(self.tonic)
            for i in range(len(self.major_steps)):
                if i != 0:
                    self.scale_midi.append(self.scale_midi[i - 1] + self.major_steps[i - 1])
                    note: list[str] = MIDI_2_NOTE[self.scale_midi[i]].split("/")
                    if len(note) == 1:  # There is only one piano key corresponding to this midi value
                        self.scale_notes.append(MIDI_2_NOTE[self.scale_midi[i]])
                    else:  # there are two piano keys corresponding to this midi value. I want the letter that comes next in the scale.
                        first_note: str = note[0][0]
                        previous_scale_note: str = MIDI_2_NOTE[self.scale_midi[i - 1]][0]  # keep only the letter of the previous scale note
                        if ord(first_note) == ord(previous_scale_note) + 1:
                            self.scale_notes.append(note[0])
                        else:
                            self.scale_notes.append(note[1])
                    
            self.scale_notes.append(f"{self.tonic[0]}{self.octave + 1}")
            self.scale_midi.append(float(NOTE_2_MIDI[self.scale_notes[-1]]))
        
        __build_scale(self, self.name)
        
        self.supertonic: str = self.scale_notes[1]
        self.mediant: str = self.scale_notes[2]
        self.subdominant: str = self.scale_notes[3]
        self.dominant: str = self.scale_notes[4]
        self.submediant: str = self.scale_notes[5]
        self.subtonic: str = self.scale_notes[6]
    
    def __str__(self) -> str:
        return f"""
         {self.tonic[0]} {self.name} Scale
             
          Tonic | {self.tonic}
     Supertonic | {self.supertonic}
        Mediant | {self.mediant}
    Subdominant | {self.subdominant}
       Dominant | {self.dominant}
     Submediant | {self.submediant}
       Subtonic | {self.subtonic}
         Octave | {self.scale_notes[-1]}
    """
    
