import esper

from ..components import sprite
from ..components import sprite_effect
from ..components import velocity
from ..components import player_bullet
from ..components import invulnerable
from ..components import health
from ..components import hurt

from . import level
from . import spawner
from . import position_constriants
from . import star_thrower
from . import pickup
from . import timeout
from . import player_move
from . import follow_path
from . import hud_display

def init_world():
    world = esper.World()

    timeout.init(world)

    spawner.init(world)
    pickup.init(world)

    invulnerable.init(world)
    player_move.init(world)
    follow_path.init(world)

    velocity.init(world)
    position_constriants.init(world)
    sprite.init(world)
    sprite_effect.init(world)

    star_thrower.init(world)
    player_bullet.init(world)

    hurt.init(world)
    health.init(world)
    level.init(world)

    hud_display.init(world)

    return world
