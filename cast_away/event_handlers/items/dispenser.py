from cast_away.event_dispatch import register_listener, COLLISION
from cast_away.components.items.dispenser import Dispenser
from cast_away.components.inventory import Inventory
from cast_away.components.items import InventoryItem
from cast_away.entities.item import create_inventory_item

def collide(world, message):
    dispenser_ent, inventory_ent = message.payload
    for dispenser in world.try_component(dispenser_ent, Dispenser):
        inventory = world.component_for_entity(inventory_ent, Inventory)
        for inventory_item_ent in inventory.item_ents:
            if inventory_item_ent is not None:
                item_name = world.component_for_entity(inventory_item_ent, InventoryItem).name
                if item_name == dispenser.item_name:
                    return
        create_inventory_item(world, dispenser_ent, inventory_ent, dispenser.item_name)

def init():
    register_listener(COLLISION, collide)