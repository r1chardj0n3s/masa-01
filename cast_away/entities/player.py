import arcade

from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.position import Position
from cast_away.components.collidable import HitCircle, Collidable
from cast_away.components.debug_primitives import debug_circle
from cast_away.components.facing import Facing
from cast_away.components.sprite import Sprite, SpriteFacing
from cast_away.components.health import Health
from cast_away.components.inventory import Inventory
from cast_away.event_dispatch import ENTITY_DIED, register_listener


def create_player(world, position, input_source):
    world.create_entity(
        Player(input_source),
        Velocity(0, 0),
        Position(position.x, position.y),
        HitCircle(radius=25),
        Collidable(),
        debug_circle(position.x, position.y),
        Facing(Facing.EAST),
        SpriteFacing(
            arcade.load_texture(
                "data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png"
            ),
            arcade.load_texture("data/kenney_robot-pack_side/robot_blueDrive1.png"),
            arcade.load_texture(
                "data/kenney_robot-pack_side/robot_blueDrive1.png",
                flipped_horizontally=True,
            ),
            arcade.load_texture(
                "data/kenney_robot-pack_side/robot_blueDrive1 - Butt.png",
                flipped_horizontally=True,
            ),
        ),
        Sprite("data/kenney_robot-pack_side/robot_blueDrive1.png", scale=0.2),
        Health(3),
        Inventory([])
    )


def player_died(world, message):
    ent = message.payload

    if not world.has_component(ent, Player):
        return

    for item_ent, item in world.get_component(Inventory):
        if item.owner_ent == ent:
            world.delete_entity(item_ent)

    world.delete_entity(ent)


def init():
    register_listener(ENTITY_DIED, player_died)
