from dataclasses import dataclass

MUSIC_VOLUME = 1
DEFAULT_MUSIC = "data/JunkyardGame1_1.mp3"

@dataclass
class Music:
    file_path: str
