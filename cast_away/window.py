import arcade

from cast_away import keyboard
from cast_away.processors import init_world
from cast_away.event_handlers import init_event_handlers
from cast_away.components.draw_layer import DrawLayer
from cast_away.components.level import CurrentLevel, Level
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
        self.world.create_entity(CurrentLevel(next_level = map_name))
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

        arcade.set_viewport(64, 1280+64, -32, 720-32)
        draw_layers = self.world.get_component(DrawLayer)
        draw_layers.sort(key=draw_layer_priority)
        for pair in draw_layers:
            entity, layer = pair
            if self.world.has_component(entity, Level):
                level = self.world.component_for_entity(entity, Level)
                if not level.loaded:
                    continue
            layer.draw()

        if self.render_debugs:
            render_debugs(self.world)
        
        arcade.set_viewport(0, 1280, 0, 720)
        for _, layer in sorted(self.world.get_component(HUDLayer), key=draw_layer_priority):
            layer.draw()
        if self.menu.show:
            self.menu.draw()


def draw_layer_priority(pair):
    e, layer = pair
    return layer.priority