from cast_away.event_dispatch import register_listener, COLLISION
from cast_away.components.bullet import Bullet
from cast_away.components.health import Health, HealthDown

def collision(world, message):
    bullet_ent, target_ent = message.payload
    if world.has_component(bullet_ent, Bullet):
        bullet = world.component_for_entity(bullet_ent, Bullet)
        if world.has_component(target_ent, bullet.target):
            health = world.component_for_entity(target_ent, Health)
            world.delete_entity(bullet_ent)
            health.effects.append(HealthDown(1))

def init():
    register_listener(COLLISION, collision)