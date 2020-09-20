import arcade

from . import keyboard

from .components import init_world
from .components.sprite import Sprite, SpriteList, SpriteFacing
from .components.facing import Facing
from .components.position import Position
from .components.velocity import Velocity
from .components.player import PlayerControlled
from .components.scene import Scene
from .components.enemy import Enemy


def load_object_layer(map, layer_name):
    layer = arcade.tilemap.get_tilemap_layer(map, layer_name)
    map_height = map.map_size.height * map.tile_size[1]
    for obj in layer.tiled_objects:
        obj.location = obj.location._replace(y=map_height - obj.location.y)
    return layer


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
                    Facing(Facing.EAST),
                    SpriteFacing(
                        arcade.load_texture("data/robot_north.png"),
                        arcade.load_texture("data/robot_east.png"),
                        arcade.load_texture("data/robot_south.png"),
                        arcade.load_texture("data/robot_west.png"),
                    ),
                    Sprite(
                        "data/kenney_robot-pack_side/robot_blueDrive1.png", scale=0.5
                    ),
                )
            if obj.name == "ENEMY_SPAWN":
                self.world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Sprite(":resources:images/enemies/bee.png", scale=0.5),
                    Enemy(),
                )

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
