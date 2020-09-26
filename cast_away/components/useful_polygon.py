from arcade.geometry import is_point_in_polygon
from euclid import LineSegment2, Point2, Vector2

class UsefulPolygon:
    def __init__(self, obj):
        self.obj = obj
        self.name = obj.name
        self.location = obj.location
        self.properties = obj.properties
        px = obj.location.x
        self.x = px
        py = obj.location.y
        self.y = py
        self.point_list = [(px + p.x, py + p.y * -1) for p in obj.points]

    def is_point_inside(self, x, y):
        return is_point_in_polygon(x, y, self.point_list)
        
    def closest_point(self, x,y):
        p=Point2(x,y)
        connects = []
        for line in self.lines():
            connects.append(line.connect(p))
        return sorted(connects, key=lambda x: abs(x))[0].p
    
    def lines(self):
        lines = []
        point_count = len(self.point_list)
        for i, p1 in enumerate(self.point_list):
            if i+1 < point_count:
                p2 = self.point_list[i+1]
                lines.append(line(p1, p2))
        lines.append(line(self.point_list[-1], self.point_list[0]))
        return lines
        

    def __repr__(self):
        return f"<Polygon name={self.name} path={self.point_list}>"

def point(p):
    return Point2(p[0], p[1])

def line(p1, p2):
    return LineSegment2(point(p1), point(p2))
