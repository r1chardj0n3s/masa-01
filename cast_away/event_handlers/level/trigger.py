from cast_away.components.level.trigger import Trigger
from cast_away.event_handlers.level import trigger_scripts
from cast_away.event_dispatch import register_listener, COLLISION

def trigger(world, message):
    source, dest = message.payload
    if world.has_component(source, Trigger):
        trigger = world.component_for_entity(source, Trigger)
        getattr(trigger_scripts, trigger.script)(world, trigger.level, trigger.obj, dest, source)

def init():
    register_listener(COLLISION, trigger)

