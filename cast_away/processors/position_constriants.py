import esper

from ..components.velocity import Velocity
from ..components.position import Position
from ..components.debug_primitives import DebugCircle
from ..components.useful_polygon import UsefulPolygon
from ..components.position_constriants import ArenaBoundary


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
