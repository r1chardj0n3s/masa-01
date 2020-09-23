import esper

from cast_away.components.player import Player
from cast_away.components.input_source import DROP 
from cast_away.components.inventory import Inventory
from cast_away.entities.inventory_item import drop_inventory_item

DROP_DEBOUNCE = 1

class DropProcessor(esper.Processor):
    def process(self, dt):
        for player, (player, inventory) in self.world.get_components(Player, Inventory):
            inventory.drop_debounce -= dt
            if inventory.drop_debounce < 0 and player.input_source.state.get(DROP):
                if len(inventory.items) > 0:
                    drop_inventory_item(self.world, inventory.items[inventory.selection])
                    inventory.drop_debounce = DROP_DEBOUNCE


def init(world):
    world.add_processor(DropProcessor())