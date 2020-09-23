import arcade
import pytiled_parser

from cast_away.components.draw_layer import DrawLayer
import cast_away.entities.level.on_load

from cast_away.entities.level.triggers import create_trigger
from cast_away.components.sprite import SpriteList
from cast_away.components.level import Level, CurrentLevel
from cast_away.components.scene import Scene
from cast_away.components.player import Player
from cast_away.components.position import Position
from cast_away.components.level.player_spawn import PlayerSpawns

from cast_away.tmx_fixes import load_object_layer

SPRITES_LAYER_Z = 50

def create_image_layer(world, tmx_map, layer, level_comp):
    world.create_entity(
        DrawLayer(
            layer.properties.get("z", 0),
            arcade.tilemap.process_layer(
                tmx_map, layer.name, hit_box_algorithm="None"
            ),
        ),
        level_comp,
    )

def map_filename(name):
    return f"data/{name}.tmx"

def unload_map(world, level_ent):
    level_comp = world.component_for_entity(level_ent, Level)
    level_comp.loaded = False

def load_map(world, current_level):
    level_name = current_level.next_level
    level_ent = None
    for e, level in world.get_component(Level):
        if level.name == level_name:
            level.loaded = True
            level_ent = e
            break
    else:
        sprite_list = SpriteList()
        tile_map = arcade.tilemap.read_tmx(map_filename(level_name))
        level_comp = Level(level_name, tile_map, True)
        level_ent = world.create_entity(level_comp)

        for obj in load_object_layer(tile_map, "OnLoad").tiled_objects:
            getattr(cast_away.entities.level.on_load, obj.name)(world, level_ent, obj)

        triggers = load_object_layer(tile_map, "Triggers")
        for obj in triggers.tiled_objects:
            create_trigger(world, level_ent, obj)

        world.create_entity(
            DrawLayer(SPRITES_LAYER_Z, sprite_list), 
            level_comp
        )
        world.create_entity(Scene(), sprite_list, level_comp)

        # add all tiled layers
        for layer in tile_map.layers:
            if isinstance(layer, (pytiled_parser.objects.TileLayer, pytiled_parser.objects.ImageLayer)):
                create_image_layer(world, tile_map, layer, level_comp)

    current_level.last_level = current_level.level_ent
    current_level.level_ent = level_ent
