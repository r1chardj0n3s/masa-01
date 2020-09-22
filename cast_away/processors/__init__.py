import esper

from ..components import player
from ..components import sprite
from ..components import sprite_effect
from ..components import velocity
from ..components import player_bullet
from ..components import invulnerable
from ..components import health
from ..components import hurt
from ..components import health_display
from ..components import joystick
from ..components import keyboard_spawn

from . import level
from . import spawner
from . import position_constriants
from . import star_thrower
from . import pickup
from . import timeout

def init_world():
    world = esper.World()

    timeout.init(world)

    spawner.init(world)
    pickup.init(world)

    invulnerable.init(world)
    player.init(world)

    velocity.init(world)
    position_constriants.init(world)
    sprite.init(world)
    sprite_effect.init(world)

    star_thrower.init(world)
    player_bullet.init(world)

    hurt.init(world)
    health.init(world)
    level.init(world)

    health_display.init(world)
    joystick.init(world)
    keyboard_spawn.init(world)

    return world
