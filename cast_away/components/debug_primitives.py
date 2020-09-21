
def debug_circle(x, y):
    return DebugCircle(x, y, 10, (255, 0, 0, 100))

class DebugCircle:
    def __init__(self, x, y, size, color, draw=True):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.draw = draw

    def __repr__(self):
        return f"<DebugCircle x={self.x} y={self.y} size={self.size} color={self.color} draw={self.draw}>"


class DebugPoly:
    def __init__(self, poly, size, color, draw=False):
        self.poly = poly
        self.size = size
        self.color = color
        self.draw = draw

    def __repr__(self):
        return f"<DebugPolygon size={self.size} color={self.color} draw={self.draw} path={self.poly}>"
