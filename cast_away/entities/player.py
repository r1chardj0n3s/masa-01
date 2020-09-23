import arcade

from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.position import Position
from cast_away.components.collidable import HitCircle, Collidable
from cast_away.components.debug_primitives import debug_circle
from cast_away.components.facing import Facing
from cast_away.components.sprite import Sprite, SpriteFacing
from cast_away.components.health import Health
from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.inventory import Inventory, InventoryItem
from cast_away.event_dispatch import ENTITY_DIED, register_listener
from cast_away.entities.hud.health_display import create_health_display
from cast_away.entities.hud.inventory_display import create_player_inventory_hud
from cast_away.components.sprite_effect import SpinEffect, SpriteEffects, ThrowToEffect
from cast_away.components.sequence import Sequence


def create_player(world, spawner, position, input_source):
    player_ent = world.create_entity(
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
        Inventory([]),
    )
    if spawner.type == "first":
        world.create_entity(
            Sequence(
                player_ent,
                SpriteEffects(
                    ThrowToEffect(1, Position(-100, 0), position, 400), SpinEffect(1, 720)
                ),
                Player(input_source),
            )
        )
    else:
        world.add_component(player_ent, Player(input_source))

    create_hud(world, player_ent)


def create_hud(world, player_ent):
    create_health_display(world, player_ent)
    create_player_inventory_hud(world, player_ent)


def player_died(world, message):
    player_entity = message.payload

    if not world.has_component(player_entity, Player):
        return

    for item_ent, item in world.get_component(InventoryItem):
        if item.owner_ent == player_entity:
            world.delete_entity(item_ent)

    for hud_ent, display in world.get_component(HealthDisplay):
        if display.player_entity == player_entity:
            world.delete_entity(hud_ent)

    world.delete_entity(player_entity)


def init():
    register_listener(ENTITY_DIED, player_died)
