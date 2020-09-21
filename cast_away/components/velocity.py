import esper
import math

from .position import Position


class Velocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"<Velocity dx={self.dx} dy={self.dy}>"

    @property
    def magnitude(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)
    @magnitude.setter
    def magnitude(self, value):
        self.normalise()
        self.dx *= value
        self.dy *= value

    def normalise(self):
        magnitude = self.magnitude
        if magnitude:
            self.dx /= magnitude
            self.dy /= magnitude


class VelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for _, (position, velocity) in self.world.get_components(Position, Velocity):
            position.x += velocity.dx * dt
            position.y += velocity.dy * dt


def init(world):
    world.add_processor(VelocityPositionProcessor())
