import arcade 
from cast_away.components.hud.inventory_display import InventoryHudDisplay, INVENTORY_X_OFFSET, INVENTORY_X_SPACING, INVENTORY_Y
from cast_away.components.hud.hud_layer import HUDLayer

def inventory_hud_sprite(path, index, sprite_list, scale):
    x_offset = INVENTORY_X_OFFSET
    x_spacing = INVENTORY_X_SPACING
    center_x = x_offset + x_spacing * index
    sprite_list.append(arcade.Sprite(path, center_x=center_x, center_y=INVENTORY_Y, scale=scale))


def create_player_inventory_hud(world, player):
    sprite_list = arcade.SpriteList()
    for i, num in enumerate(["073", "074", "075"]):
        inventory_hud_sprite(f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png", i, sprite_list, scale=0.5)
    return world.create_entity(InventoryHudDisplay(player), HUDLayer(sprite_list))