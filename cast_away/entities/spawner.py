from cast_away.components.sprite import Sprite
from cast_away.components.position import Position
from cast_away.components.spawner import PlayerSpawner, EnemySpawner
from cast_away.components.spawner import PickupSpawner
from cast_away.components.follow_path import FollowPath
from cast_away.components.enemy import Enemy
from cast_away.entities.enemy import create_enemy


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


def create_enemy_path(world, obj, level_comp):
    x, y = obj.point_list[0]
    ent = create_enemy(world, None, Position(x, y), level_comp)
    world.add_component(ent, FollowPath(obj.point_list))


def create_pickup_spawner(world, obj, level_comp):
    world.create_entity(
        PickupSpawner(obj.properties["type"]),
        Position(obj.location.x, obj.location.y),
        level_comp,
        Sprite(":resources:images/items/star.png"),
    )
