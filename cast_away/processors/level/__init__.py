import esper
import arcade
import pytiled_parser
import os

from cast_away.components.useful_polygon import UsefulPolygon
from cast_away.components.position import Position
from cast_away.components.player import Player
from cast_away.components.level.player_spawn import PlayerSpawns
from cast_away.components.level import LevelProgression, Level, LEVEL_SWAP_SOUND

from cast_away.entities.level import activate_map, deactivate_map
from cast_away.entities.sound import create_sound

def map_filename(name):
    return f"data/{name}.tmx"


class LevelProcessor(esper.Processor):
    def process(self, dt):
        for _, current_level in self.world.get_component(LevelProgression):
            if current_level.next_level is not None:
                if current_level.level_ent is not None:
                    deactivate_map(self.world, current_level.level_ent)
                activate_map(self.world, current_level)
                current_level.next_level = None
                create_sound(self.world, LEVEL_SWAP_SOUND)

            level_ent = current_level.level_ent

            for _, (_, position) in self.world.get_components(Player, Position):
                if position.level != current_level.level_ent:
                    # place active players
                    spawners = self.world.component_for_entity(level_ent, PlayerSpawns)
                    spawns = spawners.spawns
                    spawn = None
                    if current_level.last_level is not None:
                        last_level = self.world.component_for_entity(
                            current_level.last_level, Level
                        )
                        spawn = spawns.get(last_level.name)
                    if spawn is None:
                        for _, spawn in spawns.items():
                            if spawn.first:
                                break
                    position.x = spawn.x
                    position.y = spawn.y
                    position.level = level_ent


def init(world):
    world.add_processor(LevelProcessor())
