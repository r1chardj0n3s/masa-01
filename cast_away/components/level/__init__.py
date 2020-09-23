from dataclasses import dataclass

@dataclass
class Level:
    name: str
    tile_map: object
    loaded: bool = False

@dataclass
class CurrentLevel:
    next_level: str
    name: str = None
    level_ent: int = None
    last_level: int = None
