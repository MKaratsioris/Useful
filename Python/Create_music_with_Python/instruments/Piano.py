from scamp import Session
from utils.constants import RANGES, NOTE_2_MIDI
from music.MelodyLine import MelodyLine
from music.BassLine import BassLine

class Piano:
    def __init__(self, session: Session) -> None:
        self.name = "piano"
        self.session = session
        self.piano = self.session.new_part(self.name)
        self.range: list[str] = RANGES["Piano"]
        self.note: str = ""
        self.melody_line: MelodyLine = MelodyLine()
        self.chords: list[tuple[str]] = []
        self.bass_line: BassLine = BassLine()
        
    def play_note(self, note_name: str, volume: float = 1.0, duration: float = 1.0) -> None:
        """Range of notes: A1 - C8"""
        if not note_name in self.range:
            raise ValueError(f"Invalid note: {note_name}. Expected a note between A1 and C8.")
        else:
            self.piano.play_note(NOTE_2_MIDI[note_name], volume, duration)
    
    def play_chord(self, chord: tuple[str], volume: float, duration: tuple) -> None: pass
    
    def play_melody(self, melody_line: MelodyLine) -> None:
        for note in melody_line.notes:
            print(f"{note.name}\t\t{note.volume}\t\t{note.duration}")
            self.play_note(note.name, note.volume, note.duration)
    
    def play_bass(self, bass_line: BassLine) -> None:
        for note in bass_line.notes:
            self.play_note(note.name, note.volume, note.duration)