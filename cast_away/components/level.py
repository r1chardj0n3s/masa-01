import esper
import arcade

from .useful_polygon import UsefulPolygon
from .sprite import Sprite, SpriteList, SpriteFacing
from .facing import Facing
from .draw_layer import DrawLayer
from .debug_primitives import DebugCircle, DebugPoly
from .position import Position
from .position_constriants import ArenaBoundary
from .velocity import Velocity
from .player import PlayerControlled
from .scene import Scene
from .enemy import Enemy
from ..tmx_fixes import load_object_layer
from ..render_priorities import (
    BACKGROUND_LAYER,
    FOREGROUND_LAYER,
    SPRITES_LAYER
)


class Level:
    def __init__(self, name):
        self.name = name


class CurrentLevel:
    def __init__(self, name):
        self.name = name
        self.loaded = False


def debugCircle(x, y):
    return DebugCircle(x, y, 10, (255, 0, 0, 100))


class LevelProcessor(esper.Processor):
    def process(self, dt):
        for _, current_level in self.world.get_component(CurrentLevel):
            for e, level in self.world.get_component(Level):
                if level.name != current_level.name:
                    self.world.delete_entity(e, immediate=True)
            if not current_level.loaded:
                self.load_map(current_level.name)
                current_level.loaded = True

    def load_map(self, level_name):
        sprite_list = SpriteList()
        self.world.create_entity(
            DrawLayer(SPRITES_LAYER, sprite_list),
            Level(level_name)
        )
        self.world.create_entity(Scene(), sprite_list, Level(level_name))
        my_map = arcade.tilemap.read_tmx("data/{}.tmx".format(level_name))
        triggers = load_object_layer(my_map, "triggers")
        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                self.world.create_entity(
                    PlayerControlled(),
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    debugCircle(obj.location.x, obj.location.y),
                    Facing(Facing.EAST),
                    SpriteFacing(
                        arcade.load_texture("data/robot_north.png"),
                        arcade.load_texture("data/robot_east.png"),
                        arcade.load_texture("data/robot_south.png"),
                        arcade.load_texture("data/robot_west.png"),
                    ),
                    Sprite(
                        "data/kenney_robot-pack_side/robot_blueDrive1.png",
                        scale=0.5
                    ),
                    Level(level_name)
                )
            if obj.name == "ENEMY_SPAWN":
                self.world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Sprite(":resources:images/enemies/bee.png", scale=0.5),
                    Enemy(),
                    debugCircle(obj.location.x, obj.location.y),
                    Level(level_name)
                )
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
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE, draw=True),
                    Level(level_name)
                )
        self.world.create_entity(
            DrawLayer(
                BACKGROUND_LAYER,
                arcade.tilemap.process_layer(
                    my_map,
                    "ground"
                )
            ),
            Level(level_name)
        )
        self.world.create_entity(
            DrawLayer(
                FOREGROUND_LAYER,
                arcade.tilemap.process_layer(
                    my_map,
                    "foreground"
                )
            ),
            Level(level_name)
        )


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
            for ent, (poly, levelExit) in self.world.get_components(
                UsefulPolygon, LevelExit
            ):
                if poly.is_point_inside(position.x, position.y):
                    # import pdb; pdb.set_trace()
                    for _, (currentLevel,) in self.world.get_components(CurrentLevel):
                        currentLevel.name = levelExit.next_level
                        currentLevel.loaded = False


def init(world):
    world.add_processor(LevelExitProcessor())
    world.add_processor(LevelProcessor())
