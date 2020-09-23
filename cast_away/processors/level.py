import esper
import arcade
import pytiled_parser
import os

from ..components.useful_polygon import UsefulPolygon
from ..components.sprite import SpriteList
from ..components.draw_layer import DrawLayer
from ..components.position import Position
from ..components.player import Player
from ..components.scene import Scene
from ..components.level import CurrentLevel, Level, LevelExit
from ..components.spawner import PlayerSpawner

from ..entities.spawner import create_enemy_spawner, create_player_spawner, create_enemy_path
from ..entities.level import create_arena_boundary, create_exit, create_image_layer
from ..entities.props import create_spike

from ..tmx_fixes import load_object_layer
from cast_away.entities.spawner import create_pickup_spawner

SPRITES_LAYER_Z = 50


def map_filename(name):
    return f"data/{name}.tmx"


class LevelProcessor(esper.Processor):
    def process(self, dt):
        for _, current_level in self.world.get_component(CurrentLevel):
            for e, level in self.world.get_component(Level):
                if level.name != current_level.name:
                    self.world.delete_entity(e, immediate=True)
            ts = os.path.getmtime(map_filename(current_level.name))
            if ts != current_level.timestamp:
                for e, level in self.world.get_component(Level):
                    self.world.delete_entity(e, immediate=True)
                current_level.loaded = False
            if not current_level.loaded:
                self.load_map(current_level.name)
                current_level.loaded = True
            current_level.timestamp = ts

    def load_map(self, level_name):
        sprite_list = SpriteList()
        self.world.create_entity(
            DrawLayer(SPRITES_LAYER_Z, sprite_list), Level(level_name)
        )
        self.world.create_entity(Scene(), sprite_list, Level(level_name))
        my_map = arcade.tilemap.read_tmx(map_filename(level_name))
        triggers = load_object_layer(my_map, "triggers")
        level_comp = Level(level_name)

        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                create_player_spawner(self.world, obj, level_comp)
            if obj.name == "ENEMY_SPAWN":
                create_enemy_spawner(self.world, obj, level_comp)
            if obj.name == "ENEMY_PATH":
                create_enemy_path(self.world, obj, level_comp)
            if obj.name == "ARENA_BOUNDARY":
                create_arena_boundary(self.world, obj, level_comp)
            if obj.name == "EXIT":
                create_exit(self.world, obj, level_comp)
            if obj.name == "SPIKE":
                create_spike(self.world, obj, level_comp)
            if obj.name == "PICKUP":
                create_pickup_spawner(self.world, obj, level_comp)

        # add all tiled layers
        for layer in my_map.layers:
            if isinstance(layer, (pytiled_parser.objects.TileLayer, pytiled_parser.objects.ImageLayer)):
                create_image_layer(self.world, my_map, layer, level_comp)

        # place active players
        for _, current_level in self.world.get_component(CurrentLevel):
            for _, (pc, position) in self.world.get_components(Player, Position):
                for _, (player_spawner, spawn_pos) in self.world.get_components(
                    PlayerSpawner, Position
                ):
                    if player_spawner.last_level == current_level.last_level:
                        position.x = spawn_pos.x
                        position.y = spawn_pos.y


class LevelExitProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position) in self.world.get_components(Player, Position):
            for ent, (poly, level_exit) in self.world.get_components(
                UsefulPolygon, LevelExit
            ):
                if poly.is_point_inside(position.x, position.y):
                    for _, (current_level,) in self.world.get_components(CurrentLevel):
                        current_level.last_level = current_level.name
                        current_level.name = level_exit.next_level
                        current_level.loaded = False


def init(world):
    world.add_processor(LevelExitProcessor())
    world.add_processor(LevelProcessor())
