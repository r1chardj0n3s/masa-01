from .velocity import Velocity


class Facing:
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    NORTH = "NORTH"

    def __init__(self, direction):
        self.direction = Facing.EAST

    def velocity(self):
        return {
            Facing.EAST: Velocity(1, 0),
            Facing.WEST: Velocity(-1, 0),
            Facing.NORTH: Velocity(0, 1),
            Facing.SOUTH: Velocity(0, -1),
        }[self.direction]
