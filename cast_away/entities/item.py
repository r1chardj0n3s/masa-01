from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.timeout import Timeout
from cast_away.components.inventory import Inventory
from cast_away.components.items import LevelItem, InventoryItem, ITEM_DATA
from cast_away.components.player import Player

INVENTORY_SIZE = 3

def create_inventory_item(world, owner_ent, item_name):
    inventory = world.component_for_entity(owner_ent, Inventory)
    for index, ent in enumerate(inventory.item_ents):
        if ent is not None:
            continue
        _, inventory_item_data = ITEM_DATA[item_name]
        item = world.create_entity(
            InventoryItem(owner_ent=owner_ent, name=item_name),
            *[c.build() for c in inventory_item_data.component_classes]
        )
        inventory.item_ents[index] = item
        return item

def drop_inventory_item(world, inventory_item_ent):
    item_comp = world.component_for_entity(inventory_item_ent, InventoryItem)
    inventory = world.component_for_entity(item_comp.owner_ent, Inventory)
    for slot_index, ent in enumerate(inventory.item_ents):
        if ent == inventory_item_ent:
            inventory.item_ents[slot_index] = None
    world.delete_entity(inventory_item_ent)

    player_pos = world.component_for_entity(item_comp.owner_ent, Position)
    return create_level_item(
        world, 
        item_comp.name, 
        player_pos.x, 
        player_pos.y, 
        player_pos.level
    )


def create_level_item(world, name, x, y, level_ent):
    level_item_data, _ = ITEM_DATA[name]
    return world.create_entity(
        LevelItem(name),
        HitCircle(level_item_data.radius),
        Collidable(match_components=[Player]),
        Position(x, y, level_ent),
        Sprite(level_item_data.image, scale=level_item_data.scale),
        Timeout(1),
        *[c.build() for c in level_item_data.component_classes]
    )
