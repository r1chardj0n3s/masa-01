from dataclasses import dataclass

@dataclass
class Sound:
    file_path: str
    volume: float = 0.5
