import esper

from cast_away.components.player import Player
from cast_away.components.input_source import DROP, ITEM_1, ITEM_2, ITEM_3
from cast_away.components.inventory import Inventory
from cast_away.entities.item import drop_inventory_item

DROP_DEBOUNCE = 1

class DropProcessor(esper.Processor):
    def process(self, dt):
        for player, (player, inventory) in self.world.get_components(Player, Inventory):
            inventory.drop_debounce -= dt
            if inventory.drop_debounce < 0 and player.input_source.state.get(DROP):
                for i, butt in enumerate([ITEM_1, ITEM_2, ITEM_3]):
                    if player.input_source.state.get(butt):
                        try:
                            dropped_ent = inventory.item_ents[i]
                        except IndexError:
                            return
                        drop_inventory_item(self.world, dropped_ent)
                        inventory.drop_debounce = DROP_DEBOUNCE


def init(world):
    world.add_processor(DropProcessor())