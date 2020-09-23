from pydoc import locate
from cast_away.components.collidable import HitCircle, HitPoly, Collidable
from cast_away.components.level.trigger import Trigger
from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.position import Position

def create_trigger(world, level_ent, obj):
    collision_shape = None
    if isinstance(obj, UsefulPolygon):
        collision_shape = HitPoly(obj.point_list)
    else: 
        #assume circle
        collision_shape = HitCircle(obj.properties.get("radius"))
    match_components = [locate(class_name) for class_name in obj.properties.get("match_components", []).split(",")]
    avoid_components = [locate(class_name) for class_name in obj.properties.get("avoid_components", [])]
    
    world.create_entity(
        collision_shape,
        Collidable(match_components=match_components, avoid_components = avoid_components),
        Position(obj.location.x, obj.location.y, level_ent),
        Trigger(script=obj.name, obj=obj, level=level_ent)
    )
