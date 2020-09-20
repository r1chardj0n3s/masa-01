import arcade

from . import keyboard

from .components import init_world
from .components.sprite import Sprite, SpriteList
from .components.facing import Facing
from .components.debug_circles import DebugCircle
from .components.position import Position
from .components.position_constriants import ArenaBoundary
from .components.velocity import Velocity
from .components.player import PlayerControlled
from .components.scene import Scene
from .tmx_fixes import load_object_layer

class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()

    def load_map(self, level_map):
        self.scene_entity = self.world.create_entity(Scene(), SpriteList())
        self.my_map = arcade.tilemap.read_tmx("data/{}.tmx".format(level_map))
        triggers = load_object_layer(self.my_map, "triggers")
        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                self.world.create_entity(
                    PlayerControlled(),
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    DebugCircle(obj.location.x, obj.location.y,10,(255,0,0,100)),
                    Facing(Facing.EAST),
                    Sprite(
                        "data/kenney_robot-pack_side/robot_blueDrive1.png", scale=0.5
                    ),
                )
            if obj.name == "ENEMY_SPAWN":
                self.world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Sprite(":resources:images/enemies/bee.png", scale=0.5),
                    DebugCircle(obj.location.x, obj.location.y,10,(255,0,0,100)),
                )
            if obj.name == "ARENA_BOUNDARY":
                px = obj.location.x
                py = obj.location.y-195 #WAT!?
                point_list = [(px + p.x, py+p.y*-1) for p in obj.points]
                self.player_walk_poly = point_list
                self.world.create_entity(ArenaBoundary(point_list))

        self.ground_list = arcade.tilemap.process_layer(self.my_map, "ground")
        self.foreground_list = arcade.tilemap.process_layer(self.my_map, "foreground")

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
        self.ground_list.draw()
        for _, sprite_list in self.world.get_component(SpriteList):
            sprite_list._arcade_sprite_list.draw()
        self.foreground_list.draw()
        for _, debug_circle in self.world.get_component(DebugCircle):
            if debug_circle.draw:
                arcade.draw_circle_filled(debug_circle.x, debug_circle.y, debug_circle.size, debug_circle.color)
