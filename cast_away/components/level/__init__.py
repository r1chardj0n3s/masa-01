from dataclasses import dataclass


@dataclass
class Level:
    name: str
    tmx_mtime: float
    active: bool = False


@dataclass
class InLevel:
    level_ent: int


@dataclass
class LevelProgression:
    next_level: str
    name: str = None
    level_ent: int = None
    last_level: int = None
