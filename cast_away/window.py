import arcade

from cast_away import keyboard
from cast_away.processors import init_world
from cast_away.event_handlers import init_event_handlers
from cast_away.components.draw_layer import DrawLayer
from cast_away.components.level import InLevel, Level, LevelProgression
from cast_away.components.input_source import InputSource, KeyboardState
from cast_away.components.hud.hud_layer import HUDLayer

from cast_away.menu import Menu
from cast_away.render_debugs import render_debugs


class Game(arcade.Window):
    def __init__(self, map_name="1-movement"):
        super().__init__(1280, 720, "Chucked Out")
        self.world = init_world()
        init_event_handlers()
        self.world.create_entity(InputSource("Keyboard", KeyboardState()))
        self.world.create_entity(LevelProgression(next_level=map_name))
        self.menu = Menu(self, self.world)
        self.first_update = True
        self.render_debugs = False

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True
        if symbol == arcade.key.F1:
            self.render_debugs = not self.render_debugs

    def on_key_release(self, symbol, modifiers):
        del keyboard.state[symbol]

    def on_update(self, dt):
        if self.first_update or not self.menu.show:
            self.world.process(dt)
            self.first_update = False
        self.menu.update(dt)

    def on_draw(self):
        arcade.start_render()

        # set viewport to shift play area and center on map center
        arcade.set_viewport(64, 1280 + 64, -32, 720 - 32)

        draw_layers = [
            dl
            for _, (dl, il) in self.world.get_components(DrawLayer, InLevel)
                if self.world.component_for_entity(il.level_ent, Level).active
        ]
        for layer in sorted(draw_layers, key=lambda l: l.priority):
            layer.draw()
            
        if self.render_debugs:
            render_debugs(self.world)

        # reset viewport so HUD is rendered straight up
        arcade.set_viewport(0, 1280, 0, 720)

        for layer in sorted([l for _, l in self.world.get_component(HUDLayer)], key=lambda l: l.priority):
            layer.draw()

        if self.menu.show:
            self.menu.draw()
