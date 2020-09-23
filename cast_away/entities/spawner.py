from cast_away.components.sprite import Sprite
from cast_away.components.position import Position
from cast_away.components.player import Player
from cast_away.components.collidable import Collidable
from cast_away.components.spawner import PlayerSpawner, EnemySpawner
from cast_away.components.spawner import PickupSpawner
from cast_away.components.follow_path import FollowPath
from cast_away.entities.enemy import create_enemy
from cast_away.components.collidable import HitCircle

def create_enemy_spawner(world, obj, level_ent):
    world.create_entity(
        EnemySpawner(), Position(obj.location.x, obj.location.y, level_ent)
    )

def create_enemy_path(world, obj, level_ent):
    x, y = obj.point_list[0]
    ent = create_enemy(world, None, Position(x, ym, level_ent))
    world.add_component(ent, FollowPath(obj.point_list))


def create_pickup_spawner(world, obj, level_ent):
    spawner = PickupSpawner(obj.properties["type"])
    world.create_entity(
        spawner,
        HitCircle(spawner.radius),
        Collidable(match_components=[Player]),
        Position(obj.location.x, obj.location.y, level_ent),
        Sprite(spawner.image, scale=spawner.scale),
    )
