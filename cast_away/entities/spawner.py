from cast_away.components.position import Position
from cast_away.components.spawner import EnemySpawner
from cast_away.components.follow_path import FollowPath
from cast_away.entities.enemy import create_enemy


def create_enemy_spawner(world, x, y, type, level_ent):
    world.create_entity(
        EnemySpawner(),
        # Sprite("data/kenney_platformerkit2_isometric/buttonSquare_NE.png", scale=0.5),
        Position(x, y, level_ent),
    )


def create_enemy_path(world, obj, level_ent):
    x, y = obj.point_list[0]
    ent = create_enemy(world, None, Position(x, y, level_ent))
    world.add_component(ent, FollowPath(obj.point_list, 100))
