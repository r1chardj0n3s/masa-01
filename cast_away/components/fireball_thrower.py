from dataclasses import dataclass

FIREBALL_SHOOT_SOUND = ":resources:sounds/hit2.wav"
FIREBALL_IMAGE = "data/kenney_platformerpack_redux/Particles/fireball.png"


@dataclass
class FireballThrower:
    timeout: float = 0
    use_facing: bool = False
