from dataclasses import dataclass


@dataclass
class Despawn:
    after_time: float
    effect_playing: bool = False
