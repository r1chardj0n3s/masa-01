import arcade

from ..components.debug_primitives import DebugPoly
from ..components.level import LevelExit
from ..components.position_constriants import ArenaBoundary


def create_arena_boundary(world, obj, level_comp):
    world.create_entity(
        obj,
        ArenaBoundary(),
        DebugPoly(obj.point_list, 10, arcade.color.WHITE),
        level_comp,
    )


def create_exit(world, obj, level_comp):
    next_level = obj.obj.properties["next_level"]
    world.create_entity(
        obj,
        LevelExit(next_level),
        DebugPoly(obj.point_list, 10, arcade.color.WHITE),
        level_comp,
    )
