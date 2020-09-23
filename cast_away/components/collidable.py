from arcade.geometry import is_point_in_polygon

class Collidable:
    def __init__(self, match_components=[], avoid_components=[]):
        self.match_components = match_components
        self.avoid_components = avoid_components

# collidable entity will have a Position (center) and this polygon is relative to that position
class HitPoly:
    def __init__(self, point_list):
        self.point_list = point_list

    def is_point_inside(self, x, y):
        return is_point_in_polygon(x, y, self.point_list)

# collidable entity will have a Position (center) and this circle will be relative to that position
class HitCircle:
    def __init__(self, radius):
        self.radius = radius