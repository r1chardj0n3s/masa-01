from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.desired_velocity import DesiredVelocity
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.health import Health
from cast_away.components.hurt import Hurt
from cast_away.components.enemy import Enemy
from cast_away.event_dispatch import register_listener, ENTITY_DIED
from cast_away.components.items.fireball_thrower import FireballThrower
from cast_away.components.collidable import Collidable, HitCircle


def create_enemy(world, spawner_entity, position: Position):
    return world.create_entity(
        Velocity(0, 0),
        DesiredVelocity(0, 0),
        Position(position.x, position.y, position.level),
        Sprite(":resources:images/enemies/bee.png", scale=0.5),
        Enemy(spawner_entity),
        Health(1),
        Hurt(1, [Player]),
        FireballThrower(),
        Collidable(match_components=[Player]),
        HitCircle(radius=25),
    )
