import esper

from .enemy import Enemy
from .position import Position
from .sprite import Sprite


class PlayerBullet:
    ...


class PlayerBulletProcessor(esper.Processor):
    def process(self, dt):
        for bullet_ent, (bullet, position) in self.world.get_components(
            PlayerBullet, Position
        ):
            for enemy_ent, (enemy, sprite) in self.world.get_components(Enemy, Sprite):
                if sprite._arcade_sprite.collides_with_point((position.x, position.y)):
                    self.world.delete_entity(bullet_ent)
                    self.world.delete_entity(enemy_ent)
                    break


def init(world):
    world.add_processor(PlayerBulletProcessor())
