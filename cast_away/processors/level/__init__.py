import esper
import arcade
import pytiled_parser
import os

from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.sprite import SpriteList
from cast_away.components.draw_layer import DrawLayer
from cast_away.components.position import Position
from cast_away.components.player import Player
from cast_away.components.level.player_spawn import PlayerSpawns
from cast_away.components.scene import Scene
from cast_away.components.level import CurrentLevel, Level

from cast_away.entities.level import load_map, unload_map

from cast_away.entities.spawner import create_pickup_spawner

def map_filename(name):
    return f"data/{name}.tmx"

class LevelProcessor(esper.Processor):
    def process(self, dt):
        for _, current_level in self.world.get_component(CurrentLevel):
            if current_level.next_level is not None:
                if current_level.level_ent is not None:
                    unload_map(self.world, current_level.level_ent)
                load_map(self.world, current_level)
                current_level.next_level = None
            
            level_ent = current_level.level_ent

            for player_entity, (player, position) in self.world.get_components(Player, Position):
                if position.level != current_level.level_ent:
                    # place active players
                    spawners = self.world.component_for_entity(level_ent, PlayerSpawns)
                    spawns = spawners.spawns
                    spawn = None
                    if current_level.last_level is not None:
                        last_level = self.world.component_for_entity(current_level.last_level, Level)
                        spawn = spawns.get(last_level.name, None)
                    if spawn is None:
                        for name, s in spawns.items():
                            spawn = s
                            if spawn.first:
                                break
                    position.x = spawn.x
                    position.y = spawn.y
                    position.level = level_ent

def init(world):
    world.add_processor(LevelProcessor())
