import esper

from . import player
from . import gun_cooldown
from . import sprite
from . import velocity
from . import star_thrower
from . import player_bullet
from . import position_constriants


def init_world():
    world = esper.World()
    player.init(world)
    gun_cooldown.init(world)
    sprite.init(world)
    velocity.init(world)
    star_thrower.init(world)
    player_bullet.init(world)
    position_constriants.init(world)
    return world
