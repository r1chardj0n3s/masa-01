import arcade 
from cast_away.components.hud.inventory_display import InventoryHudDisplay, INVENTORY_X_OFFSET, INVENTORY_X_SPACING, INVENTORY_Y
from cast_away.components.hud.hud_layer import HUDLayer

class InventoryHudDrawable:
    def __init__(self):
        self.background_sprite_list = arcade.SpriteList()
        for i, num in enumerate(["073", "074", "075"]):
            self.background_sprite_list.append(inventory_hud_sprite(f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png", i, scale=0.5))
        self.item_sprite_list = arcade.SpriteList()
        self.selection_sprite = inventory_hud_sprite(":resources:images/items/gemYellow.png", 0, scale=0.5)

    def draw(self):
        self.background_sprite_list.draw()
        self.item_sprite_list.draw()
        self.selection_sprite.draw()

def x_for_hud_sprite(index):
    return INVENTORY_X_OFFSET + INVENTORY_X_SPACING * index

def inventory_hud_sprite(path, index, scale):
    return arcade.Sprite(path, center_x=x_for_hud_sprite(index), center_y=INVENTORY_Y, scale=scale)


def create_player_inventory_hud(world, player):
    return world.create_entity(InventoryHudDisplay(player), HUDLayer(InventoryHudDrawable()))