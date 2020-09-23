from cast_away.components.level.trigger import Trigger
from cast_away.processors.level import triggers
from cast_away.event_dispatch import register_listener, COLLISION

def trigger(world, message):
    source, dest = message.payload
    if world.has_component(source, Trigger):
        trigger = world.component_for_entity(source, Trigger)
        getattr(triggers, trigger.name)(world, trigger.level, trigger.obj, dest)

def init():
    register_listener(COLLISION, trigger)