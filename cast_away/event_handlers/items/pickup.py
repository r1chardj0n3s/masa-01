import esper

from cast_away.components.items import LevelItem
from cast_away.components.position import Position
from cast_away.components.timeout import Timeout

from cast_away.entities.item import create_inventory_item

from cast_away.event_dispatch import COLLISION, register_listener
from cast_away.entities.entity import Entity

def collision(world, message):
    level_item_ent, inventory_ent = message.payload
    for levelItem in world.try_component(level_item_ent, LevelItem):
        if not world.has_component(level_item_ent, Timeout):
            item_ent = create_inventory_item(
                world=world,
                owner_ent=inventory_ent,
                item_name=levelItem.name)
            if item_ent is not None:
                world.delete_entity(level_item_ent)


def init():
    register_listener(COLLISION, collision)
