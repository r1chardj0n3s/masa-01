
from cast_away.event_handlers.level import bullet
from cast_away.event_handlers.level import trigger
from cast_away.event_handlers import player_death
from cast_away.event_handlers import enemy

def init_event_handlers():
    bullet.init()
    trigger.init()
    player_death.init()
    enemy.init()

