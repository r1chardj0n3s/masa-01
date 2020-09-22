
from ..components.position import Position
from ..components.spawner import PlayerSpawner, EnemySpawner

def create_player_spawner(world, obj, level_comp):
    world.create_entity(PlayerSpawner(obj.properties.get('last_level')), Position(obj.location.x, obj.location.y), level_comp)

def create_enemy_spawner(world, obj, level_comp):
    world.create_entity(EnemySpawner(), Position(obj.location.x, obj.location.y), level_comp)
