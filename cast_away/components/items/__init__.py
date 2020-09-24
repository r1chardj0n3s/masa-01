from dataclasses import dataclass, field
from cast_away.components.pickups import SawThrower, LazorGun

@dataclass
class LevelItem:
    name: str

@dataclass
class InventoryItem:
    owner_ent: int
    name: str

@dataclass
class _LevelItemData:
    image: str
    component_classes: object = field(default_factory=lambda: [])
    scale: float = 0.2
    radius: float = 25

@dataclass
class _InventoryItemData:
    image: str 
    component_classes: object = field(default_factory=lambda: [])
    scale: float = 1

ITEM_DATA = {
    "saw": (
        _LevelItemData(
            image=":resources:images/enemies/saw.png",
        ), _InventoryItemData(
            image=":resources:images/enemies/saw.png",
            component_classes=[SawThrower],
        )
    ),
    "lazorgun": (
        _LevelItemData(
            image=":resources:images/items/star.png",
        ), _InventoryItemData(
            image=":resources:images/items/star.png",
            component_classes=[LazorGun],
        )
    ),
}

