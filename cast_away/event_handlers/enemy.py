from cast_away.event_dispatch import register_listener, ENTITY_DIED

from cast_away.components.enemy import Enemy
from cast_away.components.inventory import InventoryItem
from cast_away.entities.inventory_item import drop_inventory_item

def enemy_died(world, message):
    ent = message.payload

    if not world.has_component(ent, Enemy):
        return

    for item_ent, item in world.get_component(InventoryItem):
        if item.owner_ent == ent:
            drop_inventory_item(world, item_ent)

    world.delete_entity(ent)


def init():
    register_listener(ENTITY_DIED, enemy_died)