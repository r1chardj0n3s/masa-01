import math

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'<Position x={self.x} y={self.y}>'

    def distance(self, other: 'Position'):
         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
