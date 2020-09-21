
import esper

from .health import Health, HealthDown
from .useful_polygon import UsefulPolygon
from .position import Position

class Hurt:
    def __init__(self, amount, things_to_hurt):
        self.amount = amount
        self.things_to_hurt = things_to_hurt


class HurtProcessor(esper.Processor):
    def process(self, dt):
        for _, (hurt, poly) in self.world.get_components(Hurt, UsefulPolygon):
            for ent, (position, health, *rest) in self.world.get_components(Position, Health, *hurt.things_to_hurt):
                if poly.is_point_inside(position.x, position.y):
                    health.effects.append(HealthDown(hurt.amount))
        for _, (hurt, point) in self.world.get_components(Hurt, Position):
            for ent, (position, health, *rest) in self.world.get_components(Position, Health, *hurt.things_to_hurt):
                if point.distance(position) < 50:
                    health.effects.append(HealthDown(hurt.amount))


def init(world):
    world.add_processor(HurtProcessor())
