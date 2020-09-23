import arcade

from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.hud.hud_layer import HUDLayer

def create_health_display(world, player_entity):
    sprite_list = arcade.SpriteList()
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1150, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1200, center_y=50, scale=.5))
    sprite_list.append(arcade.Sprite('data/kenney_platformerpack_redux/HUD/hudHeart_full.png', center_x=1250, center_y=50, scale=.5))

    health_bar_entity = world.create_entity(HealthDisplay(player_entity), HUDLayer(sprite_list))
    return health_bar_entity
