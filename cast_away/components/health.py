
HURT_SOUND = ":resources:sounds/hurt4.wav"

class HealthDown:
    def __init__(self, amount):
        self.amount = amount


class Health:
    def __init__(self, amount):
        self.amount = amount
        self.effects = []
