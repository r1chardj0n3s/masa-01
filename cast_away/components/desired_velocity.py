import math
import euclid


class DesiredVelocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"<Desired Velocity dx={self.dx} dy={self.dy}>"

    @property
    def magnitude(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)
    @magnitude.setter
    def magnitude(self, value):
        self.normalise()
        self.dx *= value
        self.dy *= value

    def normalise(self):
        magnitude = self.magnitude
        if magnitude:
            self.dx /= magnitude
            self.dy /= magnitude

    def vector2(self):
        return euclid.Vector2(self.dx, self.dy)
