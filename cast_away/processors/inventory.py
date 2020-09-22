import arcade
import esper

from ..components.unique_item import UniqueItem
from ..components.inventory import InventoryDisplay, inventory_hud_sprite
from ..components.player import Player
from cast_away.components.draw_layer import HUDLayer

sprite_for = {
    "saw": ":resources:images/enemies/saw.png",
}

scale_for = {
    "saw": 0.6
}

class InventoryDisplayProcessor(esper.Processor):
    def process(self, dt):
        inventories = {}
        for _, (player, item) in self.world.get_components(Player, UniqueItem):
            inventories.setdefault(player, []).append(item)
        for player, inventory in inventories.items():
            sprite_list = arcade.SpriteList()
            for i, item in enumerate(inventory):
                inventory_hud_sprite(sprite_for[item.name], i, sprite_list, scale_for[item.name])
                self.world.create_entity(InventoryDisplay(sprite_list), HUDLayer(sprite_list))

def init(world):
    world.add_processor(InventoryDisplayProcessor())
