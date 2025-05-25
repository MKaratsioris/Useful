from scamp import Session, ScampInstrument
import csv

from utils.constants import RANGES, NOTE_2_MIDI

class Partitura:
    def __init__(self, tempo: int = 120, instruments: list[str] = []) -> None:
        self.tempo: int = tempo
        self.__session = Session(tempo=self.tempo)
        
        self.instruments: list[str] = [instrument.lower() for instrument in instruments]
        self.instrument_options: list[str] = [k.lower() for k in RANGES.keys()]
        self.scamp_instruments: list[ScampInstrument] = []
        for instrument in self.instruments:
            self.scamp_instruments.append(self.__session.new_part(instrument.lower()))
    
    def play_partitura(self, file_name: str) -> None:
        for instrument in self.instruments:
            self.__session.fork(self.play_instrument, args=[instrument, file_name])
        #self.__session.wait_for_children_to_finish()
            
    
    # ---------- DONE ----------
    def play_instrument(self, instrument: str, file_name: str) -> None:
        instrument_index = self.instruments.index(instrument.lower())
        print(f"\nFile: {file_name}")
        print(f"Instrument: {instrument.capitalize()}\n")
        print("No.\tNote\tVolume\tDuration")
        with open(file_name, "r") as f:
            notes_info = csv.reader(f)
            for line, row in enumerate(notes_info):
                if line != 0:
                    note, volume, duration = row
                    midi = NOTE_2_MIDI[note]
                    print(F"{line}\t{note}\t{volume}\t{duration}")
                    self.scamp_instruments[instrument_index].play_note(midi, float(volume), float(duration))
    
    def get_instruments(self) -> None:
        for i, instrument in enumerate(self.instruments):
            print(f"{i + 1}.  {instrument.capitalize()}")
    
    def add_instrument(self, instrument: str) -> None:
        if instrument.lower() in self.instrument_options:
            self.instruments.append(instrument)
            self.scamp_instruments.append(self.__session.new_part(instrument.lower()))
        else:
            raise Exception(F"Instrument {instrument} is not available")
    
    def remove_instrument(self, instrument: str) -> None:
        if instrument.lower() in self.instrument_options:
            self.instruments.remove(instrument.lower())
            self.scamp_instruments = [self.__session.new_part(instrument.lower()) for instrument in self.instruments]
        else:
            raise Exception(F"Instrument {instrument} is not part of this partitura")
    