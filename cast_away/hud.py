import arcade

from .components.draw_layer import DrawLayer
from .components.health_display import HealthDisplay

def add_health_hud(world):
    sprite_list = arcade.SpriteList()
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1150, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1200, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1250, center_y=50, scale=.5))
    world.create_entity(HealthDisplay(sprite_list), DrawLayer(9999, sprite_list))
