from arcade.geometry import is_point_in_polygon


class UsefulPolygon:
    def __init__(self, obj):
        self.obj = obj
        self.name = obj.name
        self.location = obj.location
        px = obj.location.x
        py = obj.location.y
        self.point_list = [(px + p.x, py + p.y*-1) for p in obj.points]

    def is_point_inside(self, x, y):
        return is_point_in_polygon(x, y, self.point_list)

    def __repr__(self):
        return f'<Polygon name={self.name} path={self.point_list}>'