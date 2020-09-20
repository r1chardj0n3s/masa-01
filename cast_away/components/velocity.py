import esper

from .position import Position


class Velocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"<Velocity dx={self.dx} dy={self.dy}>"

    def scale(self, amount):
        self.dx *= amount
        self.dy *= amount


class VelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for _, (position, velocity) in self.world.get_components(Position, Velocity):
            position.x += velocity.dx * dt
            position.y += velocity.dy * dt


def init(world):
    world.add_processor(VelocityPositionProcessor())
