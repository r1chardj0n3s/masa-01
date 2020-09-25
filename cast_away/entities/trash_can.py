from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.items.dispenser import Dispenser
from cast_away.components.inventory import Inventory


def create_trash_can(world, x, y, level_ent, item_name):
    return world.create_entity(
        Sprite("data/images/trash_can.png"),
        Position(x, y, level_ent),
        Collidable(match_components=[Inventory]),
        HitCircle(radius=25),
        Dispenser(item_name=item_name),
    )
