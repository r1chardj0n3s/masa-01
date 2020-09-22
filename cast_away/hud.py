import arcade

from .components.health_display import HealthDisplay
from .components.inventory import InventoryDisplay, INVENTORY_X_OFFSET, INVENTORY_X_SPACING, INVENTORY_Y, inventory_hud_sprite
from cast_away.components.draw_layer import HUDLayer

def add_hud(world):
    add_health_hud(world)
    add_inventory_hud(world)

def add_health_hud(world):
    sprite_list = arcade.SpriteList()
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1150, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1200, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1250, center_y=50, scale=.5))

    world.create_entity(HealthDisplay(sprite_list), HUDLayer(sprite_list))


def add_inventory_hud(world):
    sprite_list = arcade.SpriteList()
    for i, num in enumerate(["073", "074", "075"]):
        inventory_hud_sprite(f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png", i, sprite_list, scale=0.5)
    world.create_entity(HUDLayer(sprite_list))
    
