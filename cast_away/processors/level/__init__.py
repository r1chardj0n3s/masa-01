import esper
import arcade
import pytiled_parser
import os

from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.sprite import SpriteList
from cast_away.components.draw_layer import DrawLayer
from cast_away.components.position import Position
from cast_away.components.player import Player
from cast_away.components.scene import Scene
from cast_away.components.level import CurrentLevel, Level
from cast_away.components.spawner import PlayerSpawner

from cast_away.entities.level import load_map

from cast_away.entities.spawner import create_pickup_spawner

def map_filename(name):
    return f"data/{name}.tmx"


class LevelProcessor(esper.Processor):
    def process(self, dt):
        for _, current_level in self.world.get_component(CurrentLevel):
            for e, level in self.world.get_component(Level):
                if level.name != current_level.name:
                    self.world.delete_entity(e, immediate=True)
            ts = os.path.getmtime(map_filename(current_level.name))
            if ts != current_level.timestamp:
                for e, level in self.world.get_component(Level):
                    self.world.delete_entity(e, immediate=True)
                current_level.loaded = False
            if not current_level.loaded:
                load_map(self.world, current_level.name)
                current_level.loaded = True
            current_level.timestamp = ts

def init(world):
    world.add_processor(LevelProcessor())
