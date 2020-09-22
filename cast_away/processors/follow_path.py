import esper
from cast_away.components.position import Position
from cast_away.components.follow_path import FollowPath


class FollowPathProcessor(esper.Processor):
    def process(self, dt):
        for ent, (position, path) in self.world.get_components(Position, FollowPath):
            position.x, position.y = path.update(dt)


def init(world):
    world.add_processor(FollowPathProcessor())
