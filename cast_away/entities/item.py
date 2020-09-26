from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.timeout import Timeout
from cast_away.components.inventory import Inventory
from cast_away.components.items import LevelItem, InventoryItem, ITEM_DATA
from cast_away.components.draw_layer import ITEM_LAYER
from cast_away.components.multiplayer_identifier import MultiplayerIdentifier
from cast_away.entities.hud.inventory_display import player_base_x, INVENTORY_X_SPACING, INVENTORY_Y
from cast_away.components.sprite_effect import SpriteEffects, ThrowToEffect, FadeEffect
from cast_away.components.player import Player

INVENTORY_SIZE = 3

def create_inventory_item(world, source_ent, owner_ent, item_name):
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
        if world.has_component(owner_ent, Player):
            create_inventory_item_animation(world, source_ent, owner_ent, index, inventory_item_data)
        return item


def create_inventory_item_animation(world, source_ent, player_ent, index, inventory_item_data):
    start_pos = world.component_for_entity(source_ent, Position)
    mp = world.component_for_entity(player_ent, MultiplayerIdentifier)
    base_x = player_base_x(mp)
    end_pos = Position(base_x + 100 + INVENTORY_X_SPACING * index, INVENTORY_Y, start_pos.level)
    world.create_entity(
        Sprite(inventory_item_data.image, 0.25),
        start_pos,
        SpriteEffects(ThrowToEffect(.5, start_pos, end_pos, 50), FadeEffect(.8))
    )


def drop_inventory_item(world, inventory_item_ent):
    if inventory_item_ent is None:
        return
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
        Collidable(match_components=[Inventory]),
        Position(x, y, level_ent),
        Sprite(level_item_data.image, scale=level_item_data.scale, draw_layer=ITEM_LAYER),
        Timeout(1),
        *[c.build() for c in level_item_data.component_classes]
    )
