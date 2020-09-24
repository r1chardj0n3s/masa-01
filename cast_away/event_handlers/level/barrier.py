from cast_away.event_dispatch import register_listener, COLLISION
from cast_away.components.barrier import Barrier
from cast_away.components.velocity import BounceVelocityBack

def collision(world, message):
    source, dest = message.payload
    if not world.has_component(source, Barrier):
        return
    print("hit barrier!")
    world.create_entity(BounceVelocityBack(target_ent = dest))

def init():
    register_listener(COLLISION, collision)
