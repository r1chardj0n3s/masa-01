import esper

from . import player
from . import gun_cooldown
from . import sprite
from . import velocity
from . import star_thrower
from . import player_bullet
from . import position_constriants
from . import level
from . import invulnerable
from . import health
from . import hurt


def init_world():
    world = esper.World()

    invulnerable.init(world)
    player.init(world)
    gun_cooldown.init(world)

    velocity.init(world)
    position_constriants.init(world)
    sprite.init(world)

    star_thrower.init(world)
    player_bullet.init(world)

    hurt.init(world)
    health.init(world)
    level.init(world)
    return world
