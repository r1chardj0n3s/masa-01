from dataclasses import dataclass


@dataclass
class Bullet:
    lifespan: float
    target: object
