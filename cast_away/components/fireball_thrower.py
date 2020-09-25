from dataclasses import dataclass

@dataclass
class FireballThrower:
    timeout: float = 1
    use_facing: bool = False
