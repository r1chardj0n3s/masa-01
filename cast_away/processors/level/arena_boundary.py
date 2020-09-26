import esper
from euclid import Ray2, LineSegment2, Point2, Vector2

from cast_away.components.position import Position
from cast_away.components.level.arena_boundary import ArenaBoundary
from cast_away.components.level import Level
from cast_away.components.player import Player


class ArenaBoundaryProcessor(esper.Processor):
    def process(self, dt):
        for level_ent, (boundary, level) in self.world.get_components(
            ArenaBoundary, Level
        ):
            if level.active:
                for ent, (pos, player) in self.world.get_components(
                    Position, Player
                ):
                    if boundary.poly.is_point_inside(pos.x, pos.y):
                        return

                    closest_point = boundary.poly.closest_point(pos.x, pos.y)
                    pos.x = closest_point.x
                    pos.y = closest_point.y


def init(world):
    world.add_processor(ArenaBoundaryProcessor())
