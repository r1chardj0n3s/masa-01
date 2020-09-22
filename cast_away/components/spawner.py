class PlayerSpawner:
    def __init__(self, last_level):
        self.last_level = last_level


class EnemySpawner:
    spawning = False


class PickupSpawner:
    def __init__(self, type):
        self.type = type
