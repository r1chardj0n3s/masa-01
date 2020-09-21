
import esper

from .health import Health
from .player import PlayerControlled
from .useful_polygon import UsefulPolygon
from .position import Position
from .invulnerable import Invulnerable

class Hurt:
    def __init__(self, amount):
        self.amount = amount


class HurtProcessor(esper.Processor):
    def process(self, dt):
        for ent, (position, health) in self.world.get_components(Position, Health):
            # TODO this is a bit yuck that it's in multiple places
            if self.world.has_component(ent, Invulnerable):
                continue
            for _, (hurt, poly) in self.world.get_components(Hurt, UsefulPolygon):
                if poly.is_point_inside(position.x, position.y):
                    health.amount -= hurt.amount
                    if self.world.has_component(ent, PlayerControlled):
                        self.world.add_component(ent, Invulnerable(1))


def init(world):
    world.add_processor(HurtProcessor())
