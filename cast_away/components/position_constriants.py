import esper
import arcade
from arcade.geometry import is_point_in_polygon
from .velocity import Velocity
from .position import Position
from .debug_circles import DebugCircle

class ArenaBoundary:
  def __init__(self, polygon):
    self.polygon = polygon

  def __repr__(self):
    return f'<ArenaBoundary polygon={self.polygon}>'

class PositionConstraintProcessor(esper.Processor):
    def process(self, dt):
      for _, (boundary,) in self.world.get_components(ArenaBoundary):
        for ent, (position, velocity, debug) in self.world.get_components(Position, Velocity, DebugCircle):
          if not is_point_in_polygon(position.x, position.y, boundary.polygon):
            debug.x = position.x
            debug.y = position.y
            debug.draw = True
            position.x -= velocity.dx * dt
            position.y -= velocity.dy * dt
          else:
            debug.draw = False

def init(world):
    world.add_processor(PositionConstraintProcessor())