from dataclasses import dataclass

THROW_SOUND = ":resources:sounds/laser1.wav"

@dataclass
class Throwable():
    throw_distance: float
    throw_speed: float 

@dataclass
class LazorGun():
    ...


