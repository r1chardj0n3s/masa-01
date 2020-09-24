from .level import barrier
from .level import bullet
from .level import trigger
from . import entity_death
from . import hurt
from . import button


def init_event_handlers():
    barrier.init()
    bullet.init()
    button.init()
    trigger.init()
    entity_death.init()
    hurt.init()
