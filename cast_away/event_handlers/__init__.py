
from .level import bullet
from .level import trigger
from . import player_death
from . import enemy
from . import hurt

def init_event_handlers():
    bullet.init()
    trigger.init()
    player_death.init()
    enemy.init()
    hurt.init()

