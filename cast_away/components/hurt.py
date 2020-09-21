
import esper

from .health import Health, HealthDown
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
            for _, (hurt, poly) in self.world.get_components(Hurt, UsefulPolygon):
                if poly.is_point_inside(position.x, position.y):
                    health.effects.append(HealthDown(hurt.amount))


def init(world):
    world.add_processor(HurtProcessor())
