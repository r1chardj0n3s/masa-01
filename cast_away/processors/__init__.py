import esper

from ..components import invulnerable

from . import health
from . import level
from . import spawner
from . import pickup
from . import drop
from . import timeout
from .player import move
from . import follow_path
from . import hud_display
from . import bullet
from . import enemy_shoot
from . import collisions
from . import sprite_effect
from . import sequence
from . import sprite
from .level import arena_boundary
from . import velocity
from . import velocity_effect_processor
from . import desired_velocity


def init_world():
    world = esper.World()

    timeout.init(world)
    sequence.init(world)

    spawner.init(world)
    pickup.init(world)
    drop.init(world)

    invulnerable.init(world)
    move.init(world)
    follow_path.init(world)

    velocity.init(world)
    desired_velocity.init(world)
    sprite.init(world)
    sprite_effect.init(world)

    bullet.init(world)
    enemy_shoot.init(world)

    health.init(world)
    level.init(world)
    arena_boundary.init(world)

    hud_display.init(world)
    collisions.init(world)
    #NOTE: it is important that the velocity effect processor fires after the collision processor
    velocity_effect_processor.init(world)

    return world
