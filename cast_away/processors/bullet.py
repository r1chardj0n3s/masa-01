import esper

from cast_away.components.position import Position
from cast_away.components.bullet import Bullet
from cast_away.components.hit_emitter import HitEmitter
from cast_away.entities.emitter import create_particles


class BulletProcessor(esper.Processor):
    def process(self, dt):
        for bullet_ent, (bullet, position) in self.world.get_components(
            Bullet, Position
        ):
            bullet.lifespan -= dt
            if bullet.lifespan <= 0:
                for hit_emitter in self.world.try_component(bullet_ent, HitEmitter):
                    create_particles(self.world, hit_emitter.emitter_callable, position)
                self.world.delete_entity(bullet_ent)
                continue


def init(world):
    world.add_processor(BulletProcessor())
