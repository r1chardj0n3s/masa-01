from dataclasses import dataclass

@dataclass
class InventoryItem:
    owner_ent: int
    hud_image: str
    pickup_ent: int


@dataclass
class Inventory:
    item_ents: object
    drop_debounce: int = 0
    selection: int = None
