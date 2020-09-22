import arcade
import esper

from ..components.inventory import Inventory
from ..components.inventory import InventoryDisplay, inventory_hud_sprite
from ..components.player import Player
from cast_away.components.draw_layer import HUDLayer
from cast_away.components.pickups import Pickup

sprite_for = {
    "saw": ":resources:images/enemies/saw.png",
}

scale_for = {
    "saw": 0.6
}

class InventoryDisplayProcessor(esper.Processor):
    def __init__(self):
        self.sprite_list = arcade.SpriteList()
        self.in_list = set()

    def process(self, dt):
        inventories = {}
        for ent, item in self.world.get_component(Inventory):
            inventories.setdefault(item.owner_ent, []).append(ent)

        if not self.world.get_component(InventoryDisplay):
            self.world.create_entity(InventoryDisplay(self.sprite_list), HUDLayer(self.sprite_list))

        # TODO this only handles one player's inventory
        for player, inventory in inventories.items():
            for i, item_ent in enumerate(inventory):
                item = [i for i in self.world.components_for_entity(item_ent) if isinstance(i, Pickup)][0]
                if item.image not in self.in_list:
                    inventory_hud_sprite(item.image, i, self.sprite_list, item.hud_scale)
                    self.in_list.add(item.image)

def init(world):
    world.add_processor(InventoryDisplayProcessor())
