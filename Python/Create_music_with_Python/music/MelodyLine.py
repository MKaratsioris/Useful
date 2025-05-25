from music.Note import Note

class MelodyLine:
    def __init__(self, melody: list[Note] = []) -> None:
        self.notes: list[Note] = melody
    
    def add_note(self, note: str, volume: float = 1.0, duration: float = 1.0) -> None:
        self.notes.append(Note(note, volume, duration))
    
    def insert_note(self, position: int, note: str, volume: float = 1.0, duration: float = 1.0) -> None:
        self.notes.insert(position, Note(note, volume, duration))