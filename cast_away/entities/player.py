import arcade

from ..components.player import PlayerControlled
from ..components.velocity import Velocity
from ..components.position import Position
from ..components.debug_primitives import debug_circle
from ..components.facing import Facing
from ..components.sprite import Sprite, SpriteFacing
from ..components.health import Health


def create_player(world, position, input_source):
    world.create_entity(
        PlayerControlled(input_source),
        Velocity(0, 0),
        Position(position.x, position.y),
        debug_circle(position.x, position.y),
        Facing(Facing.EAST),
        SpriteFacing(
            arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png"),
            arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1.png"),
            arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1.png", flipped_horizontally=True),
            arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png", flipped_horizontally=True),
        ),
        Sprite(
            "data/kenney_robot-pack_side/robot_blueDrive1.png",
            scale=0.2
        ),
        Health(3)
    )
