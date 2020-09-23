class InventoryItem:
    def __init__(self, owner_ent, hud_image):
        self.owner_ent = owner_ent
        self.hud_image = hud_image


class Inventory:
    def __init__(self, item_ents, selection=None):
        self.item_ents = item_ents
        self.drop_debounce = 0
