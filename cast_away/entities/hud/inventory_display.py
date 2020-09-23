import arcade
from cast_away.components.hud.inventory_display import (
    InventoryHudDisplay,
)
from cast_away.components.hud.hud_layer import HUDLayer
from cast_away.components.multiplayer_identifier import (
    COLOURS,
    MultiplayerIdentifier,
    player_sprite_for,
)
from cast_away.components.facing import Facing

INVENTORY_X_OFFSET = 900
INVENTORY_X_SPACING = 36
INVENTORY_Y = 50


class InventoryHudDrawable:
    def __init__(self, world, player_ent):
        self.background_sprite_list = arcade.SpriteList()

        mp = world.component_for_entity(player_ent, MultiplayerIdentifier)
        index = COLOURS.index(mp.colour)
        base_x = index * 300

        self.background_sprite_list.append(
            arcade.Sprite("data/images/HUD-bg.png", center_x=base_x + 150, center_y=50)
        )

        player = player_sprite_for(mp.colour, Facing.EAST)._arcade_sprite
        player.center_x = base_x + 50
        player.center_y = INVENTORY_Y
        self.background_sprite_list.append(player)

        for i, num in enumerate(["073", "074", "075"]):
            self.background_sprite_list.append(
                inventory_hud_sprite(
                    f"data/kenney_platformerpack_industrial/platformIndustrial_{num}.png",
                    i,
                    base_x,
                    scale=0.25,
                )
            )
        self.item_sprite_list = arcade.SpriteList()

    def draw(self):
        self.background_sprite_list.draw()
        self.item_sprite_list.draw()


def x_for_hud_sprite(index):
    return 100 + INVENTORY_X_SPACING * index


def inventory_hud_sprite(path, index, x, scale):
    return arcade.Sprite(
        path, center_x=x + x_for_hud_sprite(index), center_y=INVENTORY_Y, scale=scale
    )


def create_player_inventory_hud(world, player_ent):
    return world.create_entity(
        InventoryHudDisplay(player_ent),
        HUDLayer(InventoryHudDrawable(world, player_ent)),
    )
