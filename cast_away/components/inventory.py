from dataclasses import dataclass


@dataclass
class Inventory:
    item_ents: object
    drop_debounce: int = 0
    selection: int = None
