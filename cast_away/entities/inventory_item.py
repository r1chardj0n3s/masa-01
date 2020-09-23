from cast_away.components.inventory import InventoryItem, Inventory

INVENTORY_SIZE = 3

def create_inventory_item(world, owner_ent, hud_image, inventory_item_component_classes):
    inventory = world.component_for_entity(owner_ent, Inventory)
    if len(inventory.items) < INVENTORY_SIZE:
        item = world.create_entity(InventoryItem(owner_ent=owner_ent, hud_image=hud_image), *[c() for c in inventory_item_component_classes])
        inventory.items.append(item)
        return item

def drop_inventory_item(world, item_ent):
    item_comp = world.component_for_entity(item_ent, InventoryItem)
    inventory = world.component_for_entity(item_comp.owner_ent, Inventory)
    inventory.items.remove(item_ent)
    world.delete_entity(item_ent)