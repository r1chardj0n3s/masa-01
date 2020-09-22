from cast_away.components.pickups import SawThrower, StarThrower

class PlayerSpawner:
    def __init__(self, last_level):
        self.last_level = last_level


class EnemySpawner:
    spawning = False


PICKUPS = {
    "saw": SawThrower,
    "lazorgun": StarThrower,
}


class PickupSpawner:
    def __init__(self, type):
        self.type = type
        self.component = PICKUPS[type]
