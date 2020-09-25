from dataclasses import dataclass

@dataclass
class FireballThrower:
    timeout: float = 0
    use_facing: bool = False
