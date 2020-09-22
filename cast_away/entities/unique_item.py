from ..components.unique_item import UniqueItem
from ..components.position import Position
from ..components.sprite import Sprite

def create_unique_item(world, name, level_name):
    for _, i in world.get_component(UniqueItem):
        if i.name == name:
            return
    return world.create_entity(UniqueItem(name, Position(400, 200), level_name, size=10))