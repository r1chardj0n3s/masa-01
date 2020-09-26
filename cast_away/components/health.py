HURT_SOUND = ":resources:sounds/hurt4.wav"

HEART_FULL = "data/kenney_platformerpack_redux/HUD/hudHeart_full.png"
HEART_EMPTY = "data/kenney_platformerpack_redux/HUD/hudHeart_empty.png"

class HealthDown:
    def __init__(self, amount):
        self.amount = amount


class Health:
    def __init__(self, amount):
        self.amount = amount
        self.regen_timeout = 0
        self.effects = []
