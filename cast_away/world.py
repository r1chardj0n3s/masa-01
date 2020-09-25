import esper

from cast_away.processors import add_processors
from cast_away.components.input_source import (
    InputSource,
    KeyboardState,
)
from cast_away.components.level import LevelProgression


def create_world(map_name):
    world = esper.World()
    add_processors(world)
    world.create_entity(InputSource("Keyboard", KeyboardState()))
    world.create_entity(LevelProgression(next_level=map_name))
    return world
