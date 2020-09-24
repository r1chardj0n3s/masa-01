import esper

from cast_away.components.timeout import Timeout
from cast_away.components.enemy import Enemy
from cast_away.components.level import InLevel, Level
from cast_away.components.spawner import EnemySpawner
from cast_away.components.position import Position

from cast_away.entities.enemy import create_enemy
from cast_away.components.draw_layer import DrawLayer
from cast_away.components.graphics.emitter import Emitter

from cast_away.graphics.emitters import bee_poof

class EnemySpawnProcessor(esper.Processor):
    def process(self, dt):
        for ent, (es, position) in self.world.get_components(EnemySpawner, Position):
            level = self.world.component_for_entity(position.level, Level)
            if not level.active:
                continue
            if es.spawning:
                if self.world.has_component(ent, Timeout):
                    continue

                create_enemy(self.world, ent, position)
                es.spawning = False

            for _, enemy in self.world.get_component(Enemy):
                if enemy.spawned_by == ent:
                    break
            else:
                es.spawning = True
                e = bee_poof(position)
                self.world.create_entity(DrawLayer(100, e), Emitter(e), InLevel(position.level))
                self.world.add_component(ent, Timeout(1))


def init(world):
    world.add_processor(EnemySpawnProcessor())
