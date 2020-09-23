from cast_away.components.inventory import InventoryItem, Inventory
from cast_away.components.spawner import PickupSpawner
from cast_away.components.position import Position
from cast_away.components.timeout import Timeout

INVENTORY_SIZE = 3


def create_inventory_item(
    world, owner_ent, hud_image, inventory_item_component_classes, pickup_ent
):
    inventory = world.component_for_entity(owner_ent, Inventory)
    if len(inventory.item_ents) < INVENTORY_SIZE:
        item = world.create_entity(
            InventoryItem(owner_ent=owner_ent, hud_image=hud_image, pickup_ent=pickup_ent),
            *[c() for c in inventory_item_component_classes]
        )
        inventory.item_ents.append(item)
        return item


def drop_inventory_item(world, item_ent):
    item_comp = world.component_for_entity(item_ent, InventoryItem)
    inventory = world.component_for_entity(item_comp.owner_ent, Inventory)
    inventory.item_ents.remove(item_ent)
    world.delete_entity(item_ent)
    player_pos = world.component_for_entity(item_comp.owner_ent, Position)
    spawner_pos = world.component_for_entity(item_comp.pickup_ent, Position)
    spawner_pos.x = player_pos.x
    spawner_pos.y = player_pos.y
    spawner_pos.level = player_pos.level
    world.add_component(item_comp.pickup_ent, Timeout(timeout=1))
