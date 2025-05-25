from utils.constants import NOTE_2_MIDI

class Note:
    def __init__(self, note: str, volume: float = 0.5, duration: float = 1.0) -> None:
        self.name: str = note
        self.octave: int = int(note[1])
        self.midi_value: float = float(NOTE_2_MIDI[self.name])
        self.volume: float = volume  # 0.0 to 1.0
        self.duration: float = duration  # in seconds
    
    def __str__(self) -> str:
        return f"""
             Note
             
          Name | {self.name}
        Octave | {self.octave}
        Volume | {self.volume * 100} %
      Duration | {self.duration} ♩
    Midi value | {self.midi_value}
    """    
    