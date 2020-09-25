from dataclasses import dataclass, field
from cast_away.components.items.uses import Throwable, LazorGun
from cast_away.components.timeout import Timeout
from cast_away.components.despawn import Despawn


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


@dataclass
class _ComponentTemplate:
    clazz: object
    args: object = field(default_factory=lambda: {})

    def build(self):
        return self.clazz(**self.args)


ITEM_DATA = {
    "saw": (
        _LevelItemData(
            image=":resources:images/enemies/saw.png",
            component_classes=[
                _ComponentTemplate(Despawn, {"after_time": 2})
            ],
        ), _InventoryItemData(
            image=":resources:images/enemies/saw.png",
            component_classes=[
                _ComponentTemplate(Throwable, {"throw_distance": 200, "throw_speed": 1})
            ],
        ),
    ),
    "lazorgun": (
        _LevelItemData(
            image=":resources:images/items/star.png",
        ),
        _InventoryItemData(
            image=":resources:images/items/star.png",
            component_classes=[_ComponentTemplate(LazorGun)],
        ),
    ),
}
