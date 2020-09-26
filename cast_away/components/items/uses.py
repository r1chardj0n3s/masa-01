from dataclasses import dataclass

THROW_SOUND = ":resources:sounds/laser1.wav"
LAZOR_SOUND = ":resources:sounds/laser3.wav"

@dataclass
class Throwable():
    throw_distance: float
    throw_speed: float 

@dataclass
class LazorGun():
    ...

@dataclass
class EmitOnActivate():
    emitter_factory: object
