from cast_away.components.player import PlayerControlled
import esper

from .invulnerable import Invulnerable


class HealthDown:
    def __init__(self, amount):
        self.amount = amount


class Health:
    def __init__(self, amount):
        self.amount = amount
        self.effects = []


class HealthProcessor(esper.Processor):
    def process(self, dt):
        for ent, health in self.world.get_component(Health):
            for effect in list(health.effects):
                if not self.world.has_component(ent, Invulnerable):
                    print('HURT!!', health.amount)
                    health.amount -= effect.amount
                    if self.world.has_component(ent, PlayerControlled):
                        self.world.add_component(ent, Invulnerable(1))
                health.effects.remove(effect)

            if health.amount <= 0:
                # TODO player game over if has component PlayerControlled
                self.world.delete_entity(ent)


def init(world):
    world.add_processor(HealthProcessor())
