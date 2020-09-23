import arcade

from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.hud.hud_layer import HUDLayer
from cast_away.components.multiplayer_identifier import MultiplayerIdentifier, COLOURS


def create_health_display(world, player_entity):
    mp = world.component_for_entity(player_entity, MultiplayerIdentifier)
    index = COLOURS.index(mp.colour)
    sprite_list = arcade.SpriteList()
    x = index * 300

    sprite_list.append(
        arcade.Sprite(
            "data/kenney_platformerpack_redux/HUD/hudHeart_full.png",
            center_x=x + 205,
            center_y=50,
            scale=0.25,
        )
    )
    sprite_list.append(
        arcade.Sprite(
            "data/kenney_platformerpack_redux/HUD/hudHeart_full.png",
            center_x=x + 235,
            center_y=50,
            scale=0.25,
        )
    )
    sprite_list.append(
        arcade.Sprite(
            "data/kenney_platformerpack_redux/HUD/hudHeart_full.png",
            center_x=x + 265,
            center_y=50,
            scale=0.25,
        )
    )

    health_bar_entity = world.create_entity(
        HealthDisplay(player_entity), HUDLayer(sprite_list)
    )
    return health_bar_entity
