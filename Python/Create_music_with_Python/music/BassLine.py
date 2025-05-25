from music.Note import Note

class BassLine:
    def __init__(self, bass: list[Note] = []) -> None:
        self.notes: list[Note] = bass
    
    def add_note(self, note: str, volume: float = 1.0, duration: float = 1.0, position: int = -1) -> None:
        self.notes.insert(position, Note(note, volume, duration))