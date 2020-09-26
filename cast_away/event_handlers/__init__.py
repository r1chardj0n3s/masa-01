from .level import barrier
from .level import bullet
from .level import trigger
from .items import lazorgun
from .items import pickup
from .items import drop
from .items import throwable
from .items import emit_on_activate
from .items import dispenser
from .props import goat

from . import entity_death
from . import hurt
from . import button
from . import input_event


def init_event_handlers():
    barrier.init()
    bullet.init()
    button.init()
    trigger.init()
    entity_death.init()
    hurt.init()
    input_event.init()
    lazorgun.init()
    throwable.init()
    pickup.init()
    drop.init()
    emit_on_activate.init()
    dispenser.init()
    goat.init()
