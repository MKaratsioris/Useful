# https://www.piliapp.com/symbol/music/

KEYS: dict[str, dict[str, str]] = {
    "Major": {
        "C_FLAT": "Cb",
        "G_FLAT": "Gb",
        "D_FLAT": "Db",
        "A_FLAT": "Ab",
        "E_FLAT": "Eb",
        "B_FLAT": "Bb",
        "F": "F",
        "C": "C",
        "G": "G",
        "D": "D",
        "A": "A",
        "E": "E",
        "B": "B",
        "F_SHARP": "F#",
        "C_SHARP": "C#"
    },
    "Minor": {
        "A_FLAT": "Amb",
        "E_FLAT": "Emb",
        "B_FLAT": "Bmb",
        "F": "f",
        "C": "c",
        "G": "g",
        "D": "d",
        "A": "a",
        "E": "e",
        "B": "b",
        "F_SHARP": "Fm#",
        "C_SHARP": "Cm#",
        "G_SHARP": "Gm#",
        "D_SHARP": "Dm#",
        "A_SHARP": "Am#"
    }
}

SCALES: dict[str, list[float]] = {
    "Major": [2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0],
    "Natural Minor": [2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 2.0],
    "Harmonic Minor": [2.0, 1.0, 2.0, 2.0, 1.0, 3.0, 1.0],
    "Melodic Minor": [2.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0],
    "Major Pentatonic": [2.0, 2.0, 3.0, 2.0, 3.0],
    "Minor Pentatonic": [3.0, 2.0, 2.0, 3.0, 2.0],
    "Ionian": [2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0],
    "Dorian": [2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 2.0],
    "Phrygian": [1.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0],
    "Lydian": [2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 1.0],
    "Mixolydian": [2.0, 2.0, 1.0, 2.0, 2.0, 1.0, 2.0],
    "Aeolian": [2.0, 1.0, 2.0, 2.0, 1.0, 2.0, 2.0],
    "Locrian": [1.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0],
    "Major Blues": [2.0, 1.0, 1.0, 3.0, 2.0, 3.0],
    "Minor Blues": [3.0, 2.0, 1.0, 1.0, 3.0, 2.0],
    "Jazz Major Bebop": [2.0, 2.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0],
    "Jazz Dominant Bebop": [2.0, 2.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0],
    "Jazz Whole Tone": [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
    "Jazz Whole Half Diminished": [2.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0],
    "Jazz Half Whole Diminished": [1.0, 2.0, 1.0, 2.0, 1.0, 2.0, 1.0, 2.0]
}

OCTAVES: dict[str, list[str]] = {
    "A": ["A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"],
    "B": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"],
    "C": ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    "D": ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7"],
    "E": ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7"],
    "F": ["F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7"],
    "G": ["G0", "G1", "G2", "G3", "G4", "G5", "G6", "G7"]
}

MIDI_2_NOTE: dict[int, str] = {
    21: 'A0',
    22: 'A0#/B0b',
    23: 'B0/C1b',
    24: 'B0#/C1',
    25: 'C1#/D1b',
    26: 'D1',
    27: 'D1#/E1b',
    28: 'E1/F1b',
    29: 'E1#/F1',
    30: 'F1#/G1b',
    31: 'G1',
    32: 'G1#/A1b',
    33: 'A1',
    34: 'A1#/B1b',
    35: 'B1/C2b',
    36: 'B1#/C2',
    37: 'C2#/D2b',
    38: 'D2',
    39: 'D2#/E2b',
    40: 'E2/F2b',
    41: 'E2#/F2',
    42: 'F2#/G2b',
    43: 'G2',
    44: 'G2#/A2b',
    45: 'A2',
    46: 'A2#/B2b',
    47: 'B2/C3b',
    48: 'B2#/C3',
    49: 'C3#/D3b',
    50: 'D3',
    51: 'D3#/E3b',
    52: 'E3/F3b',
    53: 'E3#/F3',
    54: 'F3#/G3b',
    55: 'G3',
    56: 'G3#/A3b',
    57: 'A3',
    58: 'A3#/B3b',
    59: 'B3/C4b',
    60: 'B3#/C4',
    61: 'C4#/D4b',
    62: 'D4',
    63: 'D4#/E4b',
    64: 'E4/F4b',
    65: 'E4#/F4',
    66: 'F4#/G4b',
    67: 'G4',
    68: 'G4#/A4b',
    69: 'A4',
    70: 'A4#/B4b',
    71: 'B4/C5b',
    72: 'B4#/C5',
    73: 'C5#/D5b',
    74: 'D5',
    75: 'D5#/E5b',
    76: 'E5/F5b',
    77: 'E5#/F5',
    78: 'F5#/G5b',
    79: 'G5',
    80: 'G5#/A5b',
    81: 'A5',
    82: 'A5#/B5b',
    83: 'B5/C6b',
    84: 'B5#/C6',
    85: 'C6#/D6b',
    86: 'D6',
    87: 'D6#/E6b',
    88: 'E6/F6b',
    89: 'E6#/F6',
    90: 'F6#/G6b',
    91: 'G6',
    92: 'G6#/A6b',
    93: 'A6',
    94: 'A6#/B6b',
    95: 'B6/C7b',
    96: 'B6#/C7',
    97: 'C7#/D7b',
    98: 'D7',
    99: 'D7#/E7b',
    100: 'E7/F7b',
    101: 'E7#/F7',
    102: 'F7#/G7b',
    103: 'G7',
    104: 'G7#/A7b',
    105: 'A7',
    106: 'A7#/B7b',
    107: 'B7/C8b',
    108: 'B7#/C8'
}

NOTE_2_MIDI: dict[str, int] = {
    "A0": 21,
    "A0#": 22,
    "B0b": 22,
    "B0": 23,
    "B0#": 24,
    "C1b": 23,  # First octave
    "C1": 24,
    "C1#": 25,
    "D1b": 25,
    "D1": 26,
    "D1#": 27,
    "E1b": 27,
    "E1": 28,
    "E1#": 29,
    "F1b": 28,
    "F1": 29,
    "F1#": 30,
    "G1b": 30,
    "G1": 31,
    "G1#": 32,
    "A1b": 32,
    "A1": 33,
    "A1#": 34,
    "B1b": 34,
    "B1": 35,
    "B1#": 36,
    "C2b": 35,  # Second octave
    "C2": 36,
    "C2#": 37,
    "D2b": 37,
    "D2": 38,
    "D2#": 39,
    "E2b": 39,
    "E2": 40,
    "E2#": 41,
    "F2b": 40,
    "F2": 41,
    "F2#": 42,
    "G2b": 42,
    "G2": 43,
    "G2#": 44,
    "A2b": 44,
    "A2": 45,
    "A2#": 46,
    "B2b": 46,
    "B2": 47,
    "B2#": 48,
    "C3b": 47,  # Third octave
    "C3": 48,
    "C3#": 49,
    "D3b": 49,
    "D3": 50,
    "D3#": 51,
    "E3b": 51,
    "E3": 52,
    "E3#": 53,
    "F3b": 52,
    "F3": 53,
    "F3#": 54,
    "G3b": 54,
    "G3": 55,
    "G3#": 56,
    "A3b": 56,
    "A3": 57,
    "A3#": 58,
    "B3b": 58,
    "B3": 59,
    "B3#": 60,
    "C4b": 59,  # Fourth octave
    "C4": 60,
    "C4#": 61,
    "D4b": 61,
    "D4": 62,
    "D4#": 63,
    "E4b": 63,
    "E4": 64,
    "E4#": 65,
    "F4b": 64,
    "F4": 65,
    "F4#": 66,
    "G4b": 66,
    "G4": 67,
    "G4#": 68,
    "A4b": 68,
    "A4": 69,
    "A4#": 70,
    "B4b": 70,
    "B4": 71,
    "B4#": 72,
    "C5b": 71,  # Fifth octave
    "C5": 72,
    "C5#": 73,
    "D5b": 73,
    "D5": 74,
    "D5#": 75,
    "E5b": 75,
    "E5": 76,
    "E5#": 77,
    "F5b": 76,
    "F5": 77,
    "F5#": 78,
    "G5b": 78,
    "G5": 79,
    "G5#": 80,
    "A5b": 80,
    "A5": 81,
    "A5#": 82,
    "B5b": 82,
    "B5": 83,
    "B5#": 84,
    "C6b": 83,  # Sixth octave
    "C6": 84,
    "C6#": 85,
    "D6b": 85,
    "D6": 86,
    "D6#": 87,
    "E6b": 87,
    "E6": 88,
    "E6#": 89,
    "F6b": 88,
    "F6": 89,
    "F6#": 90,
    "G6b": 90,
    "G6": 91,
    "G6#": 92,
    "A6b": 92,
    "A6": 93,
    "A6#": 94,
    "B6b": 94,
    "B6": 95,
    "B6#": 96,
    "C7b": 95,  # Seventh octave
    "C7": 96,
    "C7#": 97,
    "D7b": 97,
    "D7": 98,
    "D7#": 99,
    "E7b": 99,
    "E7": 100,
    "E7#": 101,
    "F7b": 100,
    "F7": 101,
    "F7#": 102,
    "G7b": 102,
    "G7": 103,
    "G7#": 104,
    "A7b": 104,
    "A7": 105,
    "A7#": 106,
    "B7b": 106,
    "B7": 107,
    "B7#": 108,
    "C8b": 107,  # Eighth octave
    "C8": 108
}

NOTES: list[str] = ['A0', 'A0#', 'B0b', 'B0', 'B0#', 'C1b', 'C1', 'C1#', 'D1b', 'D1', 'D1#', 'E1b', 'E1', 'E1#', 'F1b', 'F1', 'F1#', 'G1b', 'G1', 'G1#', 'A1b', 'A1', 'A1#', 'B1b', 'B1', 'B1#', 'C2b', 'C2', 'C2#', 'D2b', 'D2', 'D2#', 'E2b', 'E2', 'E2#', 'F2b', 'F2', 'F2#', 'G2b', 'G2', 'G2#', 'A2b', 'A2', 'A2#', 'B2b', 'B2', 'B2#', 'C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#', 'A5b', 'A5', 'A5#', 'B5b', 'B5', 'B5#', 'C6b', 'C6', 'C6#', 'D6b', 'D6', 'D6#', 'E6b', 'E6', 'E6#', 'F6b', 'F6', 'F6#', 'G6b', 'G6', 'G6#', 'A6b', 'A6', 'A6#', 'B6b', 'B6', 'B6#', 'C7b', 'C7', 'C7#', 'D7b', 'D7', 'D7#', 'E7b', 'E7', 'E7#', 'F7b', 'F7', 'F7#', 'G7b', 'G7', 'G7#', 'A7b', 'A7', 'A7#', 'B7b', 'B7', 'B7#', 'C8b', 'C8']

RANGES: dict[str, list[str]] = {
    "Piano": ['A0', 'A0#', 'B0b', 'B0', 'B0#', 'C1b', 'C1', 'C1#', 'D1b', 'D1', 'D1#', 'E1b', 'E1', 'E1#', 'F1b', 'F1', 'F1#', 'G1b', 'G1', 'G1#', 'A1b', 'A1', 'A1#', 'B1b', 'B1', 'B1#', 'C2b', 'C2', 'C2#', 'D2b', 'D2', 'D2#', 'E2b', 'E2', 'E2#', 'F2b', 'F2', 'F2#', 'G2b', 'G2', 'G2#', 'A2b', 'A2', 'A2#', 'B2b', 'B2', 'B2#', 'C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#', 'A5b', 'A5', 'A5#', 'B5b', 'B5', 'B5#', 'C6b', 'C6', 'C6#', 'D6b', 'D6', 'D6#', 'E6b', 'E6', 'E6#', 'F6b', 'F6', 'F6#', 'G6b', 'G6', 'G6#', 'A6b', 'A6', 'A6#', 'B6b', 'B6', 'B6#', 'C7b', 'C7', 'C7#', 'D7b', 'D7', 'D7#', 'E7b', 'E7', 'E7#', 'F7b', 'F7', 'F7#', 'G7b', 'G7', 'G7#', 'A7b', 'A7', 'A7#', 'B7b', 'B7', 'B7#', 'C8b', 'C8'],
    "Violin": ['G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#', 'A5b', 'A5', 'A5#', 'B5b', 'B5', 'B5#', 'C6b', 'C6', 'C6#', 'D6b', 'D6', 'D6#', 'E6b', 'E6', 'E6#', 'F6b', 'F6', 'F6#', 'G6b', 'G6', 'G6#', 'A6b', 'A6', 'A6#', 'B6b', 'B6', 'B6#', 'C7b', 'C7', 'C7#', 'D7b', 'D7', 'D7#', 'E7b', 'E7', 'E7#', 'F7b', 'F7', 'F7#', 'G7b', 'G7', 'G7#', 'A7b', 'A7', 'A7#'],
    "Viola": ['C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#'],
    "Contrabass": ['E1b', 'E1', 'E1#', 'F1b', 'F1', 'F1#', 'G1b', 'G1', 'G1#', 'A1b', 'A1', 'A1#', 'B1b', 'B1', 'B1#', 'C2b', 'C2', 'C2#', 'D2b', 'D2', 'D2#', 'E2b', 'E2', 'E2#', 'F2b', 'F2', 'F2#', 'G2b', 'G2', 'G2#', 'A2b', 'A2', 'A2#', 'B2b', 'B2', 'B2#', 'C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#'],
    "Bandoneon": ['C2b', 'C2', 'C2#', 'D2b', 'D2', 'D2#', 'E2b', 'E2', 'E2#', 'F2b', 'F2', 'F2#', 'G2b', 'G2', 'G2#', 'A2b', 'A2', 'A2#', 'B2b', 'B2', 'B2#', 'C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#', 'A5b', 'A5', 'A5#', 'B5b', 'B5', 'B5#', 'C6b', 'C6', 'C6#', 'D6b', 'D6', 'D6#', 'E6b', 'E6', 'E6#', 'F6b', 'F6', 'F6#', 'G6b', 'G6', 'G6#', 'A6b', 'A6', 'A6#', 'B6b', 'B6', 'B6#'],
    "Cello": ['C2b', 'C2', 'C2#', 'D2b', 'D2', 'D2#', 'E2b', 'E2', 'E2#', 'F2b', 'F2', 'F2#', 'G2b', 'G2', 'G2#', 'A2b', 'A2', 'A2#', 'B2b', 'B2', 'B2#', 'C3b', 'C3', 'C3#', 'D3b', 'D3', 'D3#', 'E3b', 'E3', 'E3#', 'F3b', 'F3', 'F3#', 'G3b', 'G3', 'G3#', 'A3b', 'A3', 'A3#', 'B3b', 'B3', 'B3#', 'C4b', 'C4', 'C4#', 'D4b', 'D4', 'D4#', 'E4b', 'E4', 'E4#', 'F4b', 'F4', 'F4#', 'G4b', 'G4', 'G4#', 'A4b', 'A4', 'A4#', 'B4b', 'B4', 'B4#', 'C5b', 'C5', 'C5#', 'D5b', 'D5', 'D5#', 'E5b', 'E5', 'E5#', 'F5b', 'F5', 'F5#', 'G5b', 'G5', 'G5#', 'A5b', 'A5', 'A5#', 'B5b', 'B5', 'B5#', 'C6b', 'C6', 'C6#']
}