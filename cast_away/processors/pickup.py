from cast_away.components.inventory import InventoryItem
import esper

from ..components.enemy import Enemy
from ..components.level import Level
from ..components.spawner import PickupSpawner
from ..components.position import Position

from ..entities.enemy import create_enemy
from ..entities.weapon import create_weapon
from cast_away.components.player import PlayerControlled
from cast_away.components.star_thrower import StarThrower

class PickupProcessor(esper.Processor):
    def process(self, dt):
        for _, (pickup, spos) in self.world.get_components(PickupSpawner, Position):
            for player_ent, (pc, ppos) in self.world.get_components(PlayerControlled, Position):
                if spos.distance(ppos) < 50:
                    for item in self.world.try_component(player_ent, InventoryItem):
                        if self.world.has_component(item.ent, StarThrower):
                            break
                    else:
                        thrower_ent = create_weapon(self.world, StarThrower())
                        self.world.add_component(player_ent, InventoryItem(thrower_ent))


def init(world):
    world.add_processor(PickupProcessor())
