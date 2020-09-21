import esper


class Health:
    def __init__(self, amount):
        self.amount = amount


class HealthProcessor(esper.Processor):
    def process(self, dt):
        for ent, health in self.world.get_component(Health):
            if health.amount <= 0:
                # TODO player game over if has component PlauyerControlled
                self.world.delete_entity(ent)


def init(world):
    world.add_processor(HealthProcessor())
