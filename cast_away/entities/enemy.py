from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.health import Health
from cast_away.components.hurt import Hurt
from cast_away.components.level import Level
from cast_away.components.enemy import Enemy
from cast_away.components.inventory import InventoryItem
from cast_away.event_dispatch import register_listener, ENTITY_DIED
from cast_away.components.fireball_thrower import FireballThrower


def create_enemy(world, spawner_entity, position: Position):
    return world.create_entity(
        Velocity(0, 0),
        Position(position.x, position.y, position.level),
        Sprite(":resources:images/enemies/bee.png", scale=0.5),
        Enemy(spawner_entity),
        Health(1),
        Hurt(1, [Player]),
        FireballThrower(),
    )


def enemy_died(world, message):
    ent = message.payload

    if not world.has_component(ent, Enemy):
        return

    for item_ent, item in world.get_component(InventoryItem):
        if item.owner_ent == ent:
            world.delete_entity(item_ent)

    world.delete_entity(ent)


def init():
    register_listener(ENTITY_DIED, enemy_died)
