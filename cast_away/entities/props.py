import arcade

from cast_away.components.hurt import Hurt
from cast_away.components.player import PlayerControlled
from cast_away.components.debug_primitives import DebugPoly


def create_spike(world, obj, level_comp):
    world.create_entity(
        obj,
        Hurt(1, [PlayerControlled]),
        DebugPoly(obj.point_list, 10, arcade.color.WHITE),
        level_comp,
    )
