from cast_away.components.inventory import InventoryItem, Inventory

def create_inventory_item(world, owner_ent, inventory_item_component_classes):
    inventory = world.component_for_entity(owner_ent, Inventory)
    item = world.create_entity(InventoryItem(owner_ent=owner_ent), *[c() for c in inventory_item_component_classes])
    inventory.items.append(item)
    return item
