import esper

from ..components import velocity
from ..components import invulnerable
from ..components import health
from ..components import hurt

from . import level
from . import spawner
from . import star_thrower
from . import pickup
from . import drop
from . import inventory
from . import timeout
from . import player_move
from . import follow_path
from . import hud_display
from . import bullet
from . import enemy_shoot
from . import collisions
from . import sprite_effect
from . import sequence
from . import sprite
from cast_away.processors.level import trigger_event_listener
from cast_away.processors.level import arena_boundary

def init_world():
    world = esper.World()

    timeout.init(world)
    sequence.init(world)

    spawner.init(world)
    pickup.init(world)
    drop.init(world)
    inventory.init(world)

    invulnerable.init(world)
    player_move.init(world)
    follow_path.init(world)

    velocity.init(world)
    sprite.init(world)
    sprite_effect.init(world)

    star_thrower.init(world)
    bullet.init(world)
    enemy_shoot.init(world)

    hurt.init(world)
    health.init(world)
    level.init(world)
    arena_boundary.init(world)

    hud_display.init(world)
    collisions.init(world)

    trigger_event_listener.init()

    return world
