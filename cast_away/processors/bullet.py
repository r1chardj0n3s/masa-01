import esper

from cast_away.components.health import Health, HealthDown
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.bullet import Bullet


class BulletProcessor(esper.Processor):
    def process(self, dt):
        for bullet_ent, (bullet, position) in self.world.get_components(
            Bullet, Position
        ):
            bullet.lifespan -= dt
            if bullet.lifespan <= 0:
                self.world.delete_entity(bullet_ent)
                continue
            for enemy_ent, (enemy, sprite, health) in self.world.get_components(bullet.target, Sprite, Health):
                if sprite._arcade_sprite.collides_with_point((position.x, position.y)):
                    self.world.delete_entity(bullet_ent)
                    health.effects.append(HealthDown(1))


def init(world):
    world.add_processor(BulletProcessor())
