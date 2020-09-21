import esper

from .enemy import Enemy
from .health import Health, HealthDown
from .position import Position
from .sprite import Sprite
from .invulnerable import Invulnerable


class PlayerBullet:
    lifespan = .5


class PlayerBulletProcessor(esper.Processor):
    def process(self, dt):
        for bullet_ent, (bullet, position) in self.world.get_components(
            PlayerBullet, Position
        ):
            bullet.lifespan -= dt
            if bullet.lifespan <= 0:
                self.world.delete_entity(bullet_ent)
                continue
            for enemy_ent, (enemy, sprite, health) in self.world.get_components(Enemy, Sprite, Health):
                if sprite._arcade_sprite.collides_with_point((position.x, position.y)):
                    self.world.delete_entity(bullet_ent)
                    health.effects.append(HealthDown(1))


def init(world):
    world.add_processor(PlayerBulletProcessor())
