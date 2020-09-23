import arcade

INVENTORY_X_OFFSET = 900
INVENTORY_X_SPACING = 72
INVENTORY_Y = 50


class InventoryHudDisplay:
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list

class InventoryItem:
    def __init__(self, owner_ent, hud_image):
        self.owner_ent = owner_ent
        self.hud_image = hud_image


class Inventory:
    def __init__(self, items):
        self.items = items


def inventory_hud_sprite(path, index, sprite_list, scale):
    x_offset = INVENTORY_X_OFFSET
    x_spacing = INVENTORY_X_SPACING
    center_x = x_offset + x_spacing * index
    sprite_list.append(arcade.Sprite(path, center_x=center_x, center_y=INVENTORY_Y, scale=scale))

def create_player_inventory_hud(world):
    sprite_list = arcade.SpriteList()
    for i, num in enumerate(["073", "074", "075"]):
        inventory_hud_sprite(f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png", i, sprite_list, scale=0.5)
    return InventoryDisplay(sprite_list), HUDLayer(sprite_list)