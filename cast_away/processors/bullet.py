import esper

from cast_away.components.position import Position
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


def init(world):
    world.add_processor(BulletProcessor())
