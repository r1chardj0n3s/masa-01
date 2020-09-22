import esper

from cast_away.components.spawner import PickupSpawner
from cast_away.components.inventory import Inventory


class UniqueItemProcessor(esper.Processor):
    def process(self, dt):
        for spawner_ent, spawner in self.world.get_component(PickupSpawner):
            if spawner.component.is_unique:
                for _, (inventory, item) in self.world.get_components(
                    Inventory, spawner.component
                ):
                    self.world.delete_entity(spawner_ent)


def init(world):
    world.add_processor(UniqueItemProcessor())
