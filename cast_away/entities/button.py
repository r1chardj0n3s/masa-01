from cast_away.components.button import Button
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.sprite import Sprite

def create_button(world, obj, level_ent):
    return world.create_entity(
        Button(obj.properties.get("channel"), in_level=obj.properties.get("in_level", False)), 
        Position(
            x = obj.location.x, 
            y = obj.location.y, 
            level = level_ent
        ),
        Collidable(),
        HitCircle(20),
        Sprite("data/button_sprite.png", scale=0.5),
    )
    