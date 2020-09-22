import esper

from ..components.enemy import Enemy
from ..components.level import Level
from ..components.spawner import EnemySpawner, PlayerSpawner
from ..components.position import Position

from ..entities.enemy import create_enemy

class EnemySpawnProcessor(esper.Processor):
    def process(self, dt):
        for ent, (es, position, level) in self.world.get_components(EnemySpawner, Position, Level):
            for _, enemy in self.world.get_component(Enemy):
                if enemy.spawned_by == ent:
                    break
            else:
                # TODO create after a timeout
                create_enemy(self.world, ent, position, level)

def init(world):
    world.add_processor(EnemySpawnProcessor())
