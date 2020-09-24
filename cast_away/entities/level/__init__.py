import arcade
import pytiled_parser

from cast_away.components.draw_layer import DrawLayer
import cast_away.entities.level.on_load

from cast_away.entities.level.triggers import create_trigger
from cast_away.components.sprite import SpriteList
from cast_away.components.bullet import Bullet
from cast_away.components.level import InLevel, Level

from cast_away.tmx_fixes import load_object_layer

SPRITES_LAYER_Z = 50


def create_image_layer(world, tmx_map, layer, level_comp):
    world.create_entity(
        DrawLayer(
            layer.properties.get("z", 0),
            arcade.tilemap.process_layer(tmx_map, layer.name, hit_box_algorithm="None"),
        ),
        level_comp,
    )


def map_filename(name):
    return f"data/level-{name}.tmx"


def deactivate_map(world, level_ent):
    for bullet_ent, _ in world.get_component(Bullet):
        world.delete_entity(bullet_ent)
    level_comp = world.component_for_entity(level_ent, Level)
    level_comp.active = False


def activate_map(world, current_level):
    level_name = current_level.next_level

    for level_ent, level in world.get_component(Level):
        if level.name == level_name:
            print(f"existing level comp(s) found in world: {level_name}: {level_ent}")
            level.active = True
            break
    else:
        tile_map = arcade.tilemap.read_tmx(map_filename(level_name))
        level_comp = Level(level_name, tile_map, True)
        level_ent = world.create_entity(level_comp)
        print(f"loading level from disk: {level_name}: {level_ent}")

        for obj in load_object_layer(tile_map, "OnLoad").tiled_objects:
            getattr(cast_away.entities.level.on_load, obj.name)(world, level_ent, obj)

        triggers = load_object_layer(tile_map, "Triggers")
        for obj in triggers.tiled_objects:
            create_trigger(world, level_ent, obj)

        sprite_list =  arcade.SpriteList()
        world.create_entity(DrawLayer(SPRITES_LAYER_Z, sprite_list), SpriteList(sprite_list), InLevel(level_ent))

        # add all tiled layers
        for layer in tile_map.layers:
            if isinstance(
                layer,
                (pytiled_parser.objects.TileLayer, pytiled_parser.objects.ImageLayer),
            ):
                create_image_layer(world, tile_map, layer, InLevel(level_ent))

    current_level.last_level = current_level.level_ent
    current_level.level_ent = level_ent
