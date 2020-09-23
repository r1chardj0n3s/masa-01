
import esper

from .health import Health, HealthDown
from .useful_polygon import UsefulPolygon
from .position import Position

class Hurt:
    def __init__(self, amount, things_to_hurt):
        self.amount = amount
        self.things_to_hurt = things_to_hurt
