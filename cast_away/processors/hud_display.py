import arcade
import esper

from ..components.health import Health
from ..components.hud.health_display import HealthDisplay
from ..components.player import Player
from cast_away.components.inventory import Inventory

from cast_away.components.hud.hud_layer import HUDLayer

FULL = "data/kenney_platformerpack_redux/HUD/hudHeart_full.png"
EMPTY = "data/kenney_platformerpack_redux/HUD/hudHeart_empty.png"


class HealthDisplayProcessor(esper.Processor):
    def process(self, dt):
        for _, (display, hud_layer) in self.world.get_components(HealthDisplay, HUDLayer):
            health = self.world.component_for_entity(display.player_entity, Health)
            for i in range(3):
                if health.amount > i:
                    hud_layer.drawable[i].texture = arcade.load_texture(FULL)
                else:
                    hud_layer.drawable[i].texture = arcade.load_texture(EMPTY)


def init(world):
    world.add_processor(HealthDisplayProcessor())
