import math
import euclid
from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float
    level: int
    
    def __repr__(self):
        return f'<Position x={self.x} y={self.y}>'

    def __iter__(self):
        return self.x, self.y

    def point2(self):
        return euclid.Point2(self.x, self.y)

    def distance(self, other: 'Position'):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
