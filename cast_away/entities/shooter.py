from cast_away.components.fireball_thrower import FireballThrower
from cast_away.components.facing import Facing
from cast_away.components.position import Position


def create_shooter(world, name, x, y, direction, level_ent):
    return world.create_entity(
        FireballThrower(2, True),
        Facing(direction),
        Position(x, y, level_ent),
    )
