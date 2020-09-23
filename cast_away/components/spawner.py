from cast_away.components.pickups import PICKUP_DATA

class PlayerSpawner:
    def __init__(self, last_level):
        self.last_level = last_level

class EnemySpawner:
    spawning = False

class PickupSpawner:
    def __init__(self, type):
        self.type = type
        pickup_spawner_data = PICKUP_DATA[type]
        self.image = pickup_spawner_data.image
        self.scale = pickup_spawner_data.scale
        self.radius = pickup_spawner_data.radius
        self.inventory_item_component_classes = pickup_spawner_data.inventory_item_component_classes
