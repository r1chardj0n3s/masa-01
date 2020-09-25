from .velocity import Velocity


# kenney tiles have fake isometric, 2:1 pixel ratio of diagonals
# the following transformation ensures hitting the controller diagonally
# makes the character move on a "kenney-diagonal" line as drawn on the map
DIMETRIC_FACTOR = 5.0 ** 0.5  # sqrt(5) aka diagonal of a triangle with sides 2, 1
SCALE_X = 1 / DIMETRIC_FACTOR
SCALE_Y = 1 / (DIMETRIC_FACTOR * 2)


class Facing:
    NEUTRAL = "NEUTRAL"
    EAST = "EAST"
    SOUTH_EAST = "SOUTH_EAST"
    SOUTH = "SOUTH"
    SOUTH_WEST = "SOUTH_WEST"
    WEST = "WEST"
    NORTH_WEST = "NORTH_WEST"
    NORTH = "NORTH"
    NORTH_EAST = "NORTH_EAST"

    NAMES = {
        "NEUTRAL": NEUTRAL,
        "EAST": EAST,
        "SOUTH_EAST": SOUTH_EAST,
        "SOUTH": SOUTH,
        "SOUTH_WEST": SOUTH_WEST,
        "WEST": WEST,
        "NORTH_WEST": NORTH_WEST,
        "NORTH": NORTH,
        "NORTH_EAST": NORTH_EAST,
    }

    CARDINALS = {
        (0, 0): NEUTRAL,
        (1, 0): EAST,
        (1, -1): SOUTH_EAST,
        (0, -1): SOUTH,
        (-1, -1): SOUTH_WEST,
        (-1, 0): WEST,
        (-1, 1): NORTH_WEST,
        (0, 1): NORTH,
        (1, 1): NORTH_EAST,
    }

    def __init__(self, direction=NEUTRAL):
        self.direction = direction

    @classmethod
    def from_name(cls, name):
        return cls(cls.NAMES[name])

    def set_cardinals(self, left_right, up_down):
        self.direction = self.CARDINALS[left_right, up_down]

    def velocity(self):
        return {
            Facing.NEUTRAL: Velocity(0, 0),
            Facing.EAST: Velocity(SCALE_X, 0),
            Facing.SOUTH_EAST: Velocity(SCALE_X, -SCALE_Y),
            Facing.SOUTH: Velocity(0, -SCALE_Y),
            Facing.SOUTH_WEST: Velocity(-SCALE_X, -SCALE_Y),
            Facing.WEST: Velocity(-SCALE_X, 0),
            Facing.NORTH_WEST: Velocity(-SCALE_X, SCALE_Y),
            Facing.NORTH: Velocity(0, SCALE_Y),
            Facing.NORTH_EAST: Velocity(SCALE_X, SCALE_Y),
        }[self.direction]
