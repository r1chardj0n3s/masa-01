import arcade

from .components.health_display import HealthDisplay
from .components.inventory import InventoryDisplay
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
    x_offset = 900
    x_spacing = 72
    sprite_list = arcade.SpriteList()
    def sprite(num, index):
        center_x = x_offset + x_spacing * index
        sprite_list.append(arcade.Sprite(f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png", center_x=center_x, center_y=50, scale=.5))
    for i, n in enumerate(["073", "074", "075"]):
        sprite(n, i)
    world.create_entity(InventoryDisplay(sprite_list), HUDLayer(sprite_list))
    
