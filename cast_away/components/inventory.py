import arcade

INVENTORY_X_OFFSET = 900
INVENTORY_X_SPACING = 72
INVENTORY_Y = 50

class InventoryDisplay:
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list


class InventoryItem:
    def __init__(self, ent):
        self.ent = ent

def inventory_hud_sprite(path, index, sprite_list, scale):
    x_offset = INVENTORY_X_OFFSET
    x_spacing = INVENTORY_X_SPACING
    center_x = x_offset + x_spacing * index
    sprite_list.append(arcade.Sprite(path, center_x=center_x, center_y=INVENTORY_Y, scale=scale))