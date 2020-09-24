from cast_away.components.button import Button
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.sprite import Sprite

def create_button(world, obj, level_ent):
    channel = obj.properties.get("channel")
    in_level = obj.properties.get("in_level", False)
    up_image = "data/button_up_sprite.png"
    down_image = "data/button_down_sprite.png"
    return world.create_entity(
        Button(
            channel=channel, 
            in_level=in_level,
            up_image=up_image,
            down_image=down_image
        ), 
        Position(
            x = obj.location.x, 
            y = obj.location.y, 
            level = level_ent
        ),
        Collidable(),
        HitCircle(20),
        Sprite(up_image, scale=0.5),
    )
    