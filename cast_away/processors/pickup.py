import esper

from ..components.enemy import Enemy
from ..components.level import Level
from ..components.spawner import PickupSpawner
from ..components.position import Position

from ..entities.enemy import create_enemy
from cast_away.components.player import PlayerControlled
from cast_away.components.star_thrower import StarThrower

class PickupProcessor(esper.Processor):
    def process(self, dt):
        for _, (pickup, spos) in self.world.get_components(PickupSpawner, Position):
            for ent, (pc, ppos) in self.world.get_components(PlayerControlled, Position):
                if spos.distance(ppos) < 50:
                    if not self.world.has_component(ent, StarThrower):
                        self.world.add_component(ent, StarThrower())


def init(world):
    world.add_processor(PickupProcessor())
