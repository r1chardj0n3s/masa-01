from dataclasses import dataclass


@dataclass
class Bullet:
    lifespan: int
    target: object
