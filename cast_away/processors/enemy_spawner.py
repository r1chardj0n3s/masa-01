import esper

from cast_away.components.timeout import Timeout
from cast_away.components.enemy import Enemy
from cast_away.components.level import InLevel, Level
from cast_away.components.spawner import EnemySpawner
from cast_away.components.position import Position

from cast_away.entities.enemy import create_enemy
from cast_away.entities.sequence import create_sequence
from cast_away.components.draw_layer import DrawLayer, PARTICLE_LAYER
from cast_away.components.graphics.emitter import Emitter

from cast_away.graphics.emitters import bee_poof


class EnemySpawnProcessor(esper.Processor):
    def process(self, dt):
        for ent, (es, position) in self.world.get_components(EnemySpawner, Position):
            level = self.world.component_for_entity(position.level, Level)
            if not level.active:
                continue

            if es.spawn_timer:
                es.spawn_timer -= dt

                if es.spawn_timer < 0:
                    es.spawn_timer = 0
                    create_enemy(self.world, ent, position)
            else:
                # see whether we need to spawn an enemy for this spawner
                for _, enemy in self.world.get_component(Enemy):
                    if enemy.spawned_by == ent:
                        break
                else:
                    es.spawn_timer = 5
                    e = bee_poof(position)
                    emitter = self.world.create_entity(InLevel(position.level))
                    create_sequence(self.world,
                        emitter,
                        Timeout(3),
                        DrawLayer(PARTICLE_LAYER, e),
                        Emitter(e),
                    )


def init(world):
    world.add_processor(EnemySpawnProcessor())
