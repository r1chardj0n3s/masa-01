from cast_away.event_dispatch import register_listener, COLLISION
from cast_away.components.hurt import Hurt
from cast_away.components.health import Health, HealthDown

def collide(world, message):
    source_ent, target_ent = message.payload
    if not world.has_component(source_ent, Hurt):
        return
    hurt = world.component_for_entity(source_ent, Hurt)
    for thing in hurt.things_to_hurt:
        if world.has_component(target_ent, thing):
            break;
    else:
        return
    health = world.component_for_entity(target_ent, Health)
    health.effects.append(HealthDown(hurt.amount))


def init():
    register_listener(COLLISION, collide)
