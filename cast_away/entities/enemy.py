
from cast_away.components.spawner import EnemySpawner
from ..components.player import PlayerControlled
from ..components.velocity import Velocity
from ..components.position import Position
from ..components.debug_primitives import debug_circle
from ..components.sprite import Sprite
from ..components.health import Health
from ..components.hurt import Hurt
from ..components.level_marker import Level
from ..components.enemy import Enemy


def create_enemy(world, spawner_entity, position:Position, level: Level):
    world.create_entity(
        Velocity(0, 0),
        Position(position.x, position.y),
        Sprite(":resources:images/enemies/bee.png", scale=0.5),
        Enemy(spawner_entity),
        Health(1),
        Hurt(1, [PlayerControlled]),
        debug_circle(position.x, position.y),
        level
    )
