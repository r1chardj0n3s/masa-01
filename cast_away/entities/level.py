from cast_away.components.draw_layer import DrawLayer
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


def create_tile_layer(world, tmx_map, layer, level_comp):
    world.create_entity(
                    DrawLayer(
                        layer.properties.get("z", 0),
                        arcade.tilemap.process_layer(
                            tmx_map, layer.name, hit_box_algorithm="None"
                        ),
                    ),
                    level_comp,
                )