import esper
from cast_away.components.timeout import Timeout
from cast_away.components.despawn import Despawn

class DespawnProcessor(esper.Processor):
    def process(self, dt):
        for ent, despawn in self.world.get_component(Despawn):
            if self.world.has_component(ent, Timeout):
                continue
            self.world.delete_entity(ent)


def init(world):
    world.add_processor(DespawnProcessor())
