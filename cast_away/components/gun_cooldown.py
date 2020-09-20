import esper


class GunCooldown:
    def __init__(self, timeout):
        self.timeout = timeout

class GunCooldownProcessor(esper.Processor):
    def process(self, dt):
        for ent, cooldown in self.world.get_component(GunCooldown):
            cooldown.timeout -= dt
            if cooldown.timeout <= 0:
                self.world.remove_component(ent, GunCooldown)

def init(world):
    world.add_processor(GunCooldownProcessor())
