from cast_away.event_dispatch import DROP_ITEM, register_listener

from cast_away.components.inventory import Inventory
from cast_away.entities.item import drop_inventory_item

def drop(world, message):
    player_ent = message.payload['player_ent']
    index = message.payload['index']
    inventory = world.component_for_entity(player_ent, Inventory)
    drop_inventory_item(world, inventory.item_ents[index])

def init():
    register_listener(DROP_ITEM, drop)