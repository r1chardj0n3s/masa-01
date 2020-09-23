
from .level import bullet
from .level import trigger
from . import entity_death
from . import hurt

def init_event_handlers():
    bullet.init()
    trigger.init()
    entity_death.init()
    hurt.init()
