import esper

from cast_away.components.velocity import Velocity
from cast_away.components.desired_velocity import DesiredVelocity


class DesiredVelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for _, (desired_velocity, velocity) in self.world.get_components(
            DesiredVelocity, Velocity
        ):
            velocity.dx += (desired_velocity.dx - velocity.dx) * dt
            velocity.dy += (desired_velocity.dy - velocity.dy) * dt


def init(world):
    world.add_processor(DesiredVelocityPositionProcessor())
