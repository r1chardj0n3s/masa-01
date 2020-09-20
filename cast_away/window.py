import arcade

from . import keyboard

from .components import init_world
from .components.sprite import Sprite, SpriteList, SpriteFacing
from .components.facing import Facing
from .components.debug_primitives import DebugCircle, DebugPoly
from .components.position import Position
from .components.position_constriants import ArenaBoundary
from .components.velocity import Velocity
from .components.player import PlayerControlled
from .components.scene import Scene
from .components.enemy import Enemy
from .components.level_exit import LevelExit
from .components.draw_layer import DrawLayer
from .tmx_fixes import load_object_layer
from .render_priorities import BACKGROUND_LAYER, FOREGROUND_LAYER, SPRITES_LAYER


def debugCircle(x, y):
    return DebugCircle(x, y, 10, (255, 0, 0, 100))


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()

    def load_map(self, level_map):
        sprite_list = SpriteList()
        self.world.create_entity(DrawLayer(SPRITES_LAYER, sprite_list))
        self.scene_entity = self.world.create_entity(Scene(), sprite_list)
        self.my_map = arcade.tilemap.read_tmx("data/{}.tmx".format(level_map))
        triggers = load_object_layer(self.my_map, "triggers")
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
                )
            if obj.name == "ENEMY_SPAWN":
                self.world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Sprite(":resources:images/enemies/bee.png", scale=0.5),
                    Enemy(),
                    debugCircle(obj.location.x, obj.location.y),
                )
            if obj.name == "ARENA_BOUNDARY":
                self.world.create_entity(
                    obj,
                    ArenaBoundary(),
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE)
                )
            if obj.name == "EXIT":
                next_level = obj.obj.properties['next_level']
                self.world.create_entity(
                    obj,
                    LevelExit(next_level),
                    DebugPoly(obj.point_list, 10, arcade.color.WHITE)
                )
        self.world.create_entity(
            DrawLayer(
                BACKGROUND_LAYER,
                arcade.tilemap.process_layer(
                    self.my_map,
                    "ground"
                )
            )
        )
        self.world.create_entity(
            DrawLayer(
                FOREGROUND_LAYER,
                arcade.tilemap.process_layer(
                    self.my_map,
                    "foreground"
                )
            )
        )

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
        del keyboard.state[symbol]

    def on_update(self, dt):
        self.world.process(dt)

    def on_draw(self):
        arcade.start_render()
        draw_layers = [c for (_, c) in self.world.get_component(DrawLayer)]
        draw_layers.sort(key=lambda layer: layer.priority)
        for layer in draw_layers:
            layer.draw()

        for _, debug_circle in self.world.get_component(DebugCircle):
            if debug_circle.draw:
                arcade.draw_circle_filled(
                    debug_circle.x,
                    debug_circle.y,
                    debug_circle.size,
                    debug_circle.color
                )
        for _, debug in self.world.get_component(DebugPoly):
            if debug.draw:
                arcade.draw_polygon_outline(
                    debug.poly,
                    debug.color,
                    debug.size
                )
