import esper

from cast_away.components.velocity import Velocity
from cast_away.components.position import Position
from cast_away.components.debug_primitives import DebugCircle
from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.level.arena_boundary import ArenaBoundary


class ArenaBoundaryProcessor(esper.Processor):
    def process(self, dt):
        for level_ent, boundary in self.world.get_component(ArenaBoundary):
            for ent, (position, velocity) in self.world.get_components(
                Position,
                Velocity
            ):
                if not boundary.poly.is_point_inside(
                    position.x,
                    position.y
                ):
                    position.x -= velocity.dx * dt
                    position.y -= velocity.dy * dt


def init(world):
    world.add_processor(ArenaBoundaryProcessor())
