class InventoryItem:
    def __init__(self, owner_ent, hud_image):
        self.owner_ent = owner_ent
        self.hud_image = hud_image


class Inventory:
    def __init__(self, items, selection=None):
        self.items = items
        self.drop_debounce = 0
        self.selection_debounce = 0
        self.selection = selection
