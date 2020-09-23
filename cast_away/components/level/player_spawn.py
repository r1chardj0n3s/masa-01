from dataclasses import dataclass

@dataclass
class PlayerSpawns:
    spawns: object

@dataclass
class PlayerSpawn:
    x: float
    y: float
    last_level: str
    first: bool = False
