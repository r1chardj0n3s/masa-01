import arcade
import esper

from ..components.health import Health
from ..components.health_display import HealthDisplay
from ..components.player import Player

FULL = "data/kenney_platformerpack_redux/HUD/hudHeart_full.png"
EMPTY = "data/kenney_platformerpack_redux/HUD/hudHeart_empty.png"


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
