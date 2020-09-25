from cast_away.components.level.arena_boundary import ArenaBoundary
from cast_away.components.level.player_spawn import PlayerSpawns, PlayerSpawn

from cast_away.entities.spawner import create_enemy_spawner, create_enemy_path
from cast_away.entities.button import create_button
from cast_away.entities.gate import create_gate
from cast_away.entities.item import create_level_item
from cast_away.entities.shooter import create_shooter
from cast_away.entities.trash_can import create_trash_can


def ARENA_BOUNDARY(world, level_ent, obj):
    world.add_component(level_ent, ArenaBoundary(obj))


def PLAYER_SPAWN(world, level_ent, obj):
    if not world.has_component(level_ent, PlayerSpawns):
        world.add_component(level_ent, PlayerSpawns({}))
    spawns = world.component_for_entity(level_ent, PlayerSpawns)
    last_level = obj.properties.get("last_level")
    spawns.spawns[last_level] = PlayerSpawn(
        x=obj.location.x,
        y=obj.location.y,
        last_level=last_level,
        first=obj.properties.get("first"),
    )


def ITEM(world, level_ent, obj):
    name = obj.properties["type"]
    create_level_item(world, name, obj.location.x, obj.location.y, level_ent)


def ENEMY_SPAWN(world, level_ent, obj):
    create_enemy_spawner(world, obj, level_ent)


def ENEMY_PATH(world, level_ent, obj):
    create_enemy_path(world, obj, level_ent)


def BUTTON(world, level_ent, obj):
    create_button(world, obj, level_ent)


def GATE(world, level_ent, obj):
    create_gate(world, obj, level_ent)


def SHOOTER(world, level_ent, obj):
    name = obj.properties["type"]
    direction = obj.properties["direction"]
    create_shooter(world, name, obj.location.x, obj.location.y, direction, level_ent)


def TRASH_CAN(world, level_ent, obj):
    x = obj.location.x
    y = obj.location.y
    item_name = obj.properties["item_name"]
    create_trash_can(world, x, y, level_ent, item_name)
