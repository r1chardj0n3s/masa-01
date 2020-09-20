
import arcade
import pytiled_parser.objects

def load_object_layer(map, layer_name):
    layer = arcade.tilemap.get_tilemap_layer(map, layer_name)
    map_height = map.map_size.height * map.tile_size[1]
    def fix_height(p):
        return p._replace(y = map_height - p.y)
    for obj in layer.tiled_objects:
        print(f"obj: {obj.name} location {obj.location}")
        if isinstance(obj, pytiled_parser.objects.PolygonObject):
            obj.location = fix_height(obj.location)
            # obj.points = [fix_height(p) for p in obj.points]
        elif isinstance(obj, pytiled_parser.objects.PointObject):
            obj.location = fix_height(obj.location)
        else:
            raise NotImplementedError(f"object not yet supported properly in fix_height {obj}")
        print(f"\tnew location {obj.location}")
    return layer