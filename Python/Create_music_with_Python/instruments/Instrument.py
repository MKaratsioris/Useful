from scamp import Session
from abc import ABC, abstractmethod

from music.Scale import Scale

class Instrument(ABC):
    def __init__(self, instrument: str, tempo: int = 120) -> None:
        self.name = instrument.capitalize()
        self.session = Session(tempo=tempo)
        self.instrument = self.session.new_part(instrument)
    
    def play_scale(self, scale: Scale, mode: str = "full", volume: float = 1.0, duration: float = 1.0) -> None:
        match mode:
            case "full":
                for note in scale.midi_values:
                    self.instrument.play_note(note, volume, duration)
                for note in scale.midi_values[::-1]:
                    self.instrument.play_note(note, volume, duration)
            case "ascending":
                for note in scale.midi_values:
                    self.instrument.play_note(note, volume, duration)
            case "descending":
                for note in scale.midi_values[::-1]:
                    self.instrument.play_note(note, volume, duration)
            case _:
                print(f"Invalid mode: {mode}\nPlease specify either 'full', 'ascending' or 'descending'. Try again!")
    
    @abstractmethod
    def play_note(self, note: str, volume: float, duration: float) -> None: pass
    
    @abstractmethod
    def play_chord(self, chord: tuple[str], volume: float, duration: tuple) -> None: pass
    
    @abstractmethod
    def play_melody(self, melody: tuple[str], volume: float, duration: tuple[float]) -> None: pass
    
    @abstractmethod
    def play_bass(self, bass_line: tuple[str], volume: float, duration: tuple[float]) -> None: pass