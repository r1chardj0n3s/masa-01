import arcade

INVENTORY_X_OFFSET = 900
INVENTORY_X_SPACING = 72
INVENTORY_Y = 50

class InventoryHudDisplay:
    def __init__(self, player_entity):
        self.player_entity = player_entity
