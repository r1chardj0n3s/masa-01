import esper

from . import player
from . import gun_cooldown
from . import sprite
from . import sprite_effect
from . import velocity
from . import star_thrower
from . import player_bullet
from . import position_constriants
from . import level
from . import invulnerable
from . import health
from . import hurt
from . import health_display
from . import joystick
from . import keyboard_spawn

def init_world():
    world = esper.World()

    invulnerable.init(world)
    player.init(world)
    gun_cooldown.init(world)

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
