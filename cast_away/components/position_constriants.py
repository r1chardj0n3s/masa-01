import esper
from .velocity import Velocity
from .position import Position
from .debug_primitives import DebugCircle
from .useful_polygon import UsefulPolygon


class ArenaBoundary:
    def __repr__(self):
        return '<ArenaBoundary>'


class PositionConstraintProcessor(esper.Processor):
    def process(self, dt):
        for _, (_, polygon) in self.world.get_components(
            ArenaBoundary,
            UsefulPolygon
        ):
            for ent, (position, velocity, debug) in self.world.get_components(
                Position,
                Velocity,
                DebugCircle
            ):
                if not polygon.is_point_inside(
                    position.x,
                    position.y
                ):
                    debug.x = position.x
                    debug.y = position.y
                    debug.draw = True
                    position.x -= velocity.dx * dt
                    position.y -= velocity.dy * dt
                else:
                    debug.draw = False


def init(world):
    world.add_processor(PositionConstraintProcessor())
