from cast_away.components.sprite import Sprite
from cast_away.components.position import Position
from cast_away.components.spawner import PlayerSpawner, EnemySpawner
from cast_away.components.spawner import PickupSpawner


def create_player_spawner(world, obj, level_comp):
    world.create_entity(
        PlayerSpawner(obj.properties.get("last_level")),
        Position(obj.location.x, obj.location.y),
        level_comp,
    )


def create_enemy_spawner(world, obj, level_comp):
    world.create_entity(
        EnemySpawner(), Position(obj.location.x, obj.location.y), level_comp
    )


def create_pickup_spawner(world, obj, level_comp):
    world.create_entity(
        PickupSpawner(obj.properties["type"]),
        Position(obj.location.x, obj.location.y),
        level_comp,
        Sprite(":resources:images/items/star.png"),
    )
