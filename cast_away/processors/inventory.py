import esper

from cast_away.components.input_source import SELECT_PREV, SELECT_NEXT
from cast_away.components.player import Player
from cast_away.components.inventory import InventoryItem, Inventory

SELECTION_DEBOUNCE = 0.1


class ItemSelectionProcessor(esper.Processor):
    def process(self, dt):
        for player_ent, (pc, inventory) in self.world.get_components(Player, Inventory):
            inventory.selection_debounce -= dt
            input_source = pc.input_source
            items = inventory.items
            item_count = len(items)
            if item_count == 0:
                inventory.selection = None
                return
            if item_count == 1:
                inventory.selection = 0
                return
            if inventory.selection_debounce < 0:
                if input_source.state.get(SELECT_NEXT):
                    inventory.selection_debounce = SELECTION_DEBOUNCE
                    inventory.selection += 1
                    if inventory.selection == item_count:
                        inventory.selection = 0
                elif input_source.state.get(SELECT_PREV):
                    inventory.selection_debounce = SELECTION_DEBOUNCE
                    inventory.selection -= 1
                    if inventory.selection < 0:
                        inventory.selection = item_count - 1


def init(world):
    world.add_processor(ItemSelectionProcessor())
