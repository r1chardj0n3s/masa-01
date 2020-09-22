import arcade
import esper

from .health import Health
from .player import Player

FULL = "data/kenney_platformerpack_redux/HUD/hudHeart_full.png"
EMPTY = "data/kenney_platformerpack_redux/HUD/hudHeart_empty.png"


class HealthDisplay:
    def __init__(self, sprite_list):
        self.sprite_list = sprite_list


class HealthDisplayProcessor(esper.Processor):
    def process(self, dt):
        for _, display in self.world.get_component(HealthDisplay):
            for ent, (pc, health) in self.world.get_components(Player, Health):
                for i in range(3):
                    if health.amount > i:
                        display.sprite_list[i].texture = arcade.load_texture(FULL)
                    else:
                        display.sprite_list[i].texture = arcade.load_texture(EMPTY)


def init(world):
    world.add_processor(HealthDisplayProcessor())
