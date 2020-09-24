from cast_away.event_dispatch import dispatch, register_listener, BUTTON, Message, COLLISION

from cast_away.components.button import Button
from cast_away.components.timeout import Timeout

def collision(world, message):
    source, dest = message.payload
    if not world.has_component(source, Button) or world.has_component(source, Timeout):
        return
    button = world.component_for_entity(source, Button)
    print("button pressed!")
    dispatch(world, Message(BUTTON, (source, dest, button)))
    world.add_component(source, Timeout(1))

def init():
    register_listener(COLLISION, collision)