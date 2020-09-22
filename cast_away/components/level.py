import esper
import arcade
import pytiled_parser
import os

from .useful_polygon import UsefulPolygon
from .sprite import  SpriteList
from .draw_layer import DrawLayer
from .debug_primitives import  DebugPoly
from .position import Position
from .position_constriants import ArenaBoundary
from .player import PlayerControlled
from .scene import Scene
from .hurt import Hurt
from .spawner import PlayerSpawner

from ..entities import spawner

from ..tmx_fixes import load_object_layer
from .level_marker import Level

SPRITES_LAYER_Z = 50

class CurrentLevel:
    def __init__(self, name):
        self.name = name
        self.last_level = name
        self.loaded = False
        self.timestamp = None


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
            DrawLayer(SPRITES_LAYER_Z, sprite_list),
            Level(level_name)
        )
        self.world.create_entity(Scene(), sprite_list, Level(level_name))
        my_map = arcade.tilemap.read_tmx(map_filename(level_name))
        triggers = load_object_layer(my_map, "triggers")
        level_comp = Level(level_name)

        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                spawner.create_player_spawner(self.world, obj, level_comp)

            if obj.name == "ENEMY_SPAWN":
                spawner.create_enemy_spawner(self.world, obj, level_comp)

            if obj.name == "ARENA_BOUNDARY":
                self.world.create_entity(
                    obj,
                    ArenaBoundary(),
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE),
                    Level(level_name)
                )
            if obj.name == "EXIT":
                next_level = obj.obj.properties['next_level']
                self.world.create_entity(
                    obj,
                    LevelExit(next_level),
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE),
                    Level(level_name)
                )
            if obj.name == "SPIKE":
                self.world.create_entity(
                    obj,
                    Hurt(1, [PlayerControlled]),
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE),
                    Level(level_name)
                )

        # add all tiled layers
        for layer in my_map.layers:
            if isinstance(layer, pytiled_parser.objects.TileLayer):
                self.world.create_entity(
                    DrawLayer(
                        layer.properties.get('z', 0),
                        arcade.tilemap.process_layer(
                            my_map,
                            layer.name,
                            hit_box_algorithm='None'
                        )
                    ),
                    Level(level_name)
                )

        # place active players
        for _, (current_level) in self.world.get_component(CurrentLevel):
            for _, (pc, position) in self.world.get_components(PlayerControlled, Position):
                for _, (player_spawner, spawn_pos) in self.world.get_components(PlayerSpawner, Position):
                    if player_spawner.last_level == current_level.last_level:
                        position.x = spawn_pos.x
                        position.y = spawn_pos.y


class LevelExit:
    def __init__(self, next_level):
        self.next_level = next_level

    def __repr__(self):
        return '<LevelExit next_level={self.next_level}>'


class LevelExitProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position) in self.world.get_components(
            PlayerControlled, Position
        ):
            for ent, (poly, level_exit) in self.world.get_components(
                UsefulPolygon, LevelExit
            ):
                if poly.is_point_inside(position.x, position.y):
                    # import pdb; pdb.set_trace()
                    for _, (current_level,) in self.world.get_components(CurrentLevel):
                        current_level.last_level = current_level.name
                        current_level.name = level_exit.next_level
                        current_level.loaded = False


def init(world):
    world.add_processor(LevelExitProcessor())
    world.add_processor(LevelProcessor())
