import esper
from cast_away.components.timeout import Timeout


class TimeoutProcessor(esper.Processor):
    def process(self, dt):
        for ent, cooldown in self.world.get_component(Timeout):
            cooldown.timeout -= dt
            if cooldown.timeout <= 0:
                self.world.remove_component(ent, Timeout)

def init(world):
    world.add_processor(TimeoutProcessor())
