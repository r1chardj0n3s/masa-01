from dataclasses import dataclass


@dataclass
class Trigger:
    script: str
    level: int
    obj: object
