from cast_away.event_dispatch import USE_ITEM, register_listener
from cast_away.components.sprite import Sprite
from cast_away.components.position import Position
from cast_away.components.bullet import Bullet
from cast_away.components.enemy import Enemy
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.facing import Facing
from cast_away.components.timeout import Timeout
from cast_away.components.items.uses import LazorGun


def use_lazorgun(world, message):
    if not world.has_component(message.payload['item_ent'], LazorGun):
        return
    if world.has_component(message.payload['item_ent'], Timeout):
        return

    player_ent = message.payload['player_ent']
    position = world.component_for_entity(player_ent, Position)
    facing = world.component_for_entity(player_ent, Facing)
    velocity = facing.velocity()
    velocity.magnitude = 1000
    world.create_entity(
        Sprite(":resources:images/items/star.png", scale=0.5),
        Position(x=position.x, y=position.y, level=position.level),
        velocity,
        Bullet(0.5, Enemy),
        Collidable(match_components=[Enemy]),
        HitCircle(radius=20),
    )
    world.add_component(message.payload['item_ent'], Timeout(0.5))


def init():
    register_listener(USE_ITEM, use_lazorgun)
