import esper

from cast_away.components.position import Position
from cast_away.components.velocity import Velocity


class VelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for _, (position, velocity) in self.world.get_components(Position, Velocity):
            print('hi')
            position.x += velocity.dx * dt
            position.y += velocity.dy * dt


def init(world):
    world.add_processor(VelocityPositionProcessor())
