import esper

from cast_away.components.velocity import BounceVelocityBack
from cast_away.components.position import Position
from cast_away.components.debug_primitives import DebugCircle
from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.level.arena_boundary import ArenaBoundary
from cast_away.components.level import Level
from cast_away.components.player import Player


class ArenaBoundaryProcessor(esper.Processor):
    def process(self, dt):
        for level_ent, (boundary, level) in self.world.get_components(
            ArenaBoundary, Level
        ):
            if level.active:
                for ent, (position, player) in self.world.get_components(
                    Position, Player
                ):
                    if not boundary.poly.is_point_inside(position.x, position.y):
                        self.world.create_entity(BounceVelocityBack(target_ent = ent))


def init(world):
    world.add_processor(ArenaBoundaryProcessor())
