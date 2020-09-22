import esper
import arcade
import pytiled_parser
import os

from .useful_polygon import UsefulPolygon
from .sprite import Sprite, SpriteList, SpriteFacing
from .input_source import KeyboardInputSource
from .facing import Facing
from .draw_layer import DrawLayer
from .debug_primitives import DebugCircle, DebugPoly
from .position import Position
from .position_constriants import ArenaBoundary
from .velocity import Velocity
from .player import PlayerControlled
from .scene import Scene
from .enemy import Enemy
from .health import Health
from .hurt import Hurt
from .spawner import PlayerSpawner, EnemySpawner
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
        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                player_spawner = PlayerSpawner(
                   obj.location.x,
                   obj.location.y,
                   level_name,
                   obj.properties.get("last_level")
                )
                self.world.create_entity(player_spawner, Level(level_name))
               
            if obj.name == "ENEMY_SPAWN":
                enemy_spawner = EnemySpawner(obj.location.x, obj.location.y, level_name)
                self.world.create_entity(enemy_spawner, Level(level_name))
                enemy_spawner.spawn(self.world)

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
        # place players
        for _, (pc, position) in self.world.get_components(PlayerControlled, Position):
            for _, spawner in self.world.get_component(PlayerSpawner):
                if spawner.last_level == pc.level_name:
                    position.x = spawner.x
                    position.y = spawner.y
                    pc.level_name = level_name



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
