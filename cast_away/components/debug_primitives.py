class DebugCircle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.draw = False

    def __repr__(self):
        return f"<DebugCircle x={self.x} y={self.y} size={self.size} color={self.color} draw={self.draw}>"


class DebugPoly:
    def __init__(self, poly, size, color):
        self.poly = poly
        self.size = size
        self.color = color
        self.draw = False

    def __repr__(self):
        return f"<DebugPolygon size={self.size} color={self.color} draw={self.draw} path={self.poly}>"
