from dataclasses import dataclass, field


@dataclass
class Inventory:
    item_ents: object = field(default_factory=lambda:[None, None, None])
    drop_debounce: int = 0
    selection: int = None
