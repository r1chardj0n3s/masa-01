import esper

from cast_away.components.items import LevelItem, PICKUP_SOUND
from cast_away.components.position import Position
from cast_away.components.timeout import Timeout

from cast_away.entities.item import create_inventory_item
from cast_away.entities.sound import create_sound

from cast_away.event_dispatch import COLLISION, register_listener
from cast_away.entities.entity import Entity

def collision(world, message):
    level_item_ent, inventory_ent = message.payload
    for levelItem in world.try_component(level_item_ent, LevelItem):
        if not world.has_component(level_item_ent, Timeout):
            item_ent = create_inventory_item(
                world,
                level_item_ent,
                inventory_ent,
                levelItem.name)
            if item_ent is not None:
                world.delete_entity(level_item_ent)
                create_sound(world, PICKUP_SOUND)


def init():
    register_listener(COLLISION, collision)
