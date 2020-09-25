from arcade.geometry import is_point_in_polygon
from dataclasses import dataclass, field


@dataclass
class Collidable:
    match_components: object = field(default_factory=lambda: [])
    avoid_components: object = field(default_factory=lambda: [])


# collidable entity will have a Position (center) and this polygon is relative to that position
@dataclass
class HitPoly:
    point_list: object

    def is_point_inside(self, x, y):
        return is_point_in_polygon(x, y, self.point_list)


# collidable entity will have a Position (center) and this circle will be relative to that position
@dataclass
class HitCircle:
    radius: float
