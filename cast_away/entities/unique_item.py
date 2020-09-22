from ..components.unique_item import UniqueItem
from ..components.position import Position
from ..components.sprite import Sprite

def create_unique_item(world, level_name):
    return world.create_entity(UniqueItem("saw", Position(400, 200), level_name))