import arcade
from .player import PlayerControlled
from .velocity import Velocity
from .position import Position
from .debug_primitives import debug_circle
from .facing import Facing
from .sprite import Sprite, SpriteFacing
from .health import Health
from .hurt import Hurt
from .level_marker import Level
from .enemy import Enemy


class PlayerSpawner:
    def __init__(self, x, y, last_level):
        self.x = x
        self.y = y
        self.last_level = last_level

    def spawn(self, world, input_source):
        world.create_entity(
            PlayerControlled(input_source),
            Velocity(0, 0),
            Position(self.x, self.y),
            debug_circle(self.x, self.y),
            Facing(Facing.EAST),
            SpriteFacing(
                arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png"),
                arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1.png"),
                arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1.png", flipped_horizontally=True),
                arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png", flipped_horizontally=True),
            ),
            Sprite(
                "data/kenney_robot-pack_side/robot_blueDrive1.png",
                scale=0.3
            ),
            Health(3)
        )

class EnemySpawner:
    def __init__(self, x, y, level_name):
        self.x = x
        self.y = y
        self.level_name = level_name

    def spawn(self, world):
        world.create_entity(
            Velocity(0, 0),
            Position(self.x, self.y),
            Sprite(":resources:images/enemies/bee.png", scale=0.5),
            Enemy(),
            Health(1),
            Hurt(1, [PlayerControlled]),
            debug_circle(self.x, self.y),
            Level(self.level_name)
        )