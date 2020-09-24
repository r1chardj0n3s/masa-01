from cast_away.event_dispatch import (
    dispatch,
    register_listener,
    BUTTON,
    Message,
    COLLISION,
)

from cast_away.components.button import Button, ButtonChannelListener
from cast_away.components.timeout import Timeout
from cast_away.components.level import Level


def collision(world, message):
    source, dest = message.payload
    if not world.has_component(source, Button) or world.has_component(source, Timeout):
        return
    button = world.component_for_entity(source, Button)
    dispatch(world, Message(BUTTON, (source, dest, button)))
    world.add_component(source, Timeout(1))


def button_channel_activated(world, message):
    source, dest, button = message.payload
    for ent, listener in world.get_component(ButtonChannelListener):
        if listener.channel == button.channel:
            if listener.level_ent is not None:
                if not world.component_for_entity(listener.level_ent, Level).active:
                    return
            listener.script(world, ent, dest)


def init():
    register_listener(COLLISION, collision)
    register_listener(BUTTON, button_channel_activated)
