from pydoc import locate

from cast_away.components.button import Button
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.sprite import Sprite

def locate_classes(properties, key):
    classnames = properties.get(key, "")
    if classnames == "":
        return []
    classnamelist = classnames.split(",")
    return [locate(name) for name in classnamelist]

def create_button(world, obj, level_ent):
    properties = obj.properties
    if properties is None:
        properties = {}
    channel = properties.get("channel")
    in_level = properties.get("in_level", False)

    match_components = locate_classes(properties, "match_components")
    avoid_components = locate_classes(properties, "avoid_components")
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
        Collidable(
            match_components=match_components,
            avoid_components=avoid_components
        ),
        HitCircle(20),
        Sprite(up_image, scale=0.5),
    )
    