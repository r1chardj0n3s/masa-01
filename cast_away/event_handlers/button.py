from cast_away.event_dispatch import (
    dispatch,
    register_listener,
    CHANNEL,
    Message,
    COLLISION,
)

from cast_away.components.button import Button, Channel, ChannelListener
from cast_away.components.timeout import Timeout
from cast_away.components.position import Position


def collision(world, message):
    source, dest = message.payload
    if not world.has_component(source, Button) or world.has_component(source, Timeout):
        return
    button = world.component_for_entity(source, Button)
    if button.down_state:
        return
    button.down_state = True
    level_ent = None
    if button.in_level:
        level_ent = world.component_for_entity(source, Position).level
    dispatch(world, Message(CHANNEL, (source, dest, Channel(button.channel, level_ent))))
    world.add_component(source, Timeout(1))
    # print(f"button {source} {button} pressed by {dest}")


def channel_activated(world, message):
    source, dest, channel = message.payload
    listeners = []
    if channel.level_ent is not None:
        listeners = [(e, c) for e, (c,p) in world.get_components(ChannelListener, Position) if p.level == channel.level_ent]
    else:
        listeners = world.get_component(ChannelListener)
    for ent, listener in listeners:
        if listener.channel == channel.channel:
            if listener.level_ent is not None:
                level = world.component_for_entity(ent, Position).level
                if channel.level_ent != level:
                    continue
            listener.script(world, ent, dest)


def init():
    register_listener(COLLISION, collision)
    register_listener(CHANNEL, channel_activated)
