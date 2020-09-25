import arcade
import esper

from cast_away.components.health import Health
from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.hud.inventory_display import InventoryHudDisplay
from cast_away.components.inventory import Inventory
from cast_away.components.items import InventoryItem, ITEM_DATA

from cast_away.components.hud.hud_layer import HUDLayer
from cast_away.entities.hud.inventory_display import inventory_hud_sprite
from cast_away.components.multiplayer_identifier import MultiplayerIdentifier, COLOURS

FULL = "data/kenney_platformerpack_redux/HUD/hudHeart_full.png"
EMPTY = "data/kenney_platformerpack_redux/HUD/hudHeart_empty.png"


class HealthDisplayProcessor(esper.Processor):
    def process(self, dt):
        for _, (display, hud_layer) in self.world.get_components(
            HealthDisplay, HUDLayer
        ):
            health = self.world.component_for_entity(display.player_entity, Health)
            for i in range(3):
                if health.amount > i:
                    hud_layer.drawable[i].texture = arcade.load_texture(FULL)
                else:
                    hud_layer.drawable[i].texture = arcade.load_texture(EMPTY)


class InventoryDisplayProcessor(esper.Processor):
    def process(self, dt):
        for _, (display, hud_layer) in self.world.get_components(
            InventoryHudDisplay, HUDLayer
        ):
            sprite_list = hud_layer.drawable.item_sprite_list

            def set_sprite_at(i, base_x, image):
                if i < len(sprite_list):
                    sprite_list[i].texture = arcade.load_texture(image)
                    sprite_list[i].alpha = 255
                else:
                    sprite_list.append(
                        inventory_hud_sprite(image, i, base_x, scale=0.25)
                    )

            def hide_sprite_at(i):
                if i < len(sprite_list):
                    sprite_list[i].alpha = 0

            inventory = self.world.component_for_entity(
                display.player_entity, Inventory
            )
            mp = self.world.component_for_entity(
                display.player_entity, MultiplayerIdentifier
            )
            for i, item_entity in enumerate(inventory.item_ents):
                if item_entity is None:
                    hide_sprite_at(i)
                    continue
                inventory_item = self.world.component_for_entity(
                    item_entity, InventoryItem
                )
                _, inventory_item_data = ITEM_DATA[inventory_item.name]
                index = COLOURS.index(mp.colour)
                base_x = index * 300
                set_sprite_at(i, base_x, inventory_item_data.image)


def init(world):
    world.add_processor(HealthDisplayProcessor())
    world.add_processor(InventoryDisplayProcessor())
