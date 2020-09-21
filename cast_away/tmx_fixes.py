
import arcade
import pytiled_parser.objects
from .components.useful_polygon import UsefulPolygon


def load_object_layer(map, layer_name):
    layer = arcade.tilemap.get_tilemap_layer(map, layer_name)
    map_height = map.map_size.height * map.tile_size[1] / 2 #only for staggered orientation WOOT!

    def fix_height(p):
        return p._replace(y=map_height - p.y)

    def convert(obj):
        if isinstance(obj, pytiled_parser.objects.PolygonObject):
            obj.location = fix_height(obj.location)
            return UsefulPolygon(obj)
        elif isinstance(obj, pytiled_parser.objects.PointObject):
            obj.location = fix_height(obj.location)
            return obj
        else:
            raise NotImplementedError(
                f"object not yet supported properly in fix_height {obj}"
            )

    layer.tiled_objects = [convert(obj) for obj in layer.tiled_objects]
    return layer
