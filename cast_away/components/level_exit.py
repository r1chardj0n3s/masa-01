import esper
from .player import PlayerControlled
from .position import Position


class LevelExit:
    def __init__(self, next_level):
        self.next_level = next_level

    def __repr__(self):
        return '<LevelExit next_level={self.next_level}>'


class LevelExitProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position, levelExit) in self.world.get_components(
            PlayerControlled, Position, LevelExit
        ):
            ...
