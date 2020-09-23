from cast_away.components.level.arena_boundary import ArenaBoundary
from cast_away.components.level.player_spawn import PlayerSpawns, PlayerSpawn

from cast_away.entities.spawner import create_enemy_spawner, create_enemy_path, create_pickup_spawner

def ARENA_BOUNDARY(world, level_ent, obj):
    world.add_component(level_ent, ArenaBoundary(obj))

def PLAYER_SPAWN(world, level_ent, obj):
    if not world.has_component(level_ent, PlayerSpawns):
        world.add_component(level_ent, PlayerSpawns({}))
    spawns = world.component_for_entity(level_ent, PlayerSpawns)
    spawns.spawns[obj.properties.get("last_level")] = PlayerSpawn(
        x = obj.location.x, 
        y = obj.location.y, 
        last_level = obj.properties.get("last_level"),
        first = obj.properties.get("first")
    )

def PICKUP(world, level_ent, obj):
    create_pickup_spawner(world, obj, level_ent)

def ENEMY_SPAWN(world, level_ent, obj):
    create_enemy_spawner(self.world, obj, level_ent)

def ENEMY_PATH(world, level_ent, obj):
    create_enemy_path(self.world, obj, level_ent)
