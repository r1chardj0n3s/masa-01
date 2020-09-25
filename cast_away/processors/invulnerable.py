import esper

from cast_away.components.invulnerable import Invulnerable


class InvulnerableProcessor(esper.Processor):
    def process(self, dt):
        for ent, invuln in self.world.get_component(Invulnerable):
            invuln.lifespan -= dt
            if invuln.lifespan <= 0:
                self.world.remove_component(ent, Invulnerable)


def init(world):
    world.add_processor(InvulnerableProcessor())
