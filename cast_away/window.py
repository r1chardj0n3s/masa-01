import arcade


from . import keyboard
from .processors import init_world
from .components.draw_layer import DrawLayer
from .components.debug_primitives import DebugCircle, DebugPoly
from .components.level import CurrentLevel
from .components.input_source import KeyboardInputSource

from .hud import add_health_hud
from .menu import Menu
from cast_away.components.draw_layer import HUDLayer

class Game(arcade.Window):
    def __init__(self, map_name="1-movement"):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()
        self.world.create_entity(KeyboardInputSource())
        self.world.create_entity(CurrentLevel(map_name))
        add_health_hud(self.world)
        self.menu = Menu(self, self.world)
        self.first_update = True

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True

    def on_key_release(self, symbol, modifiers):
        del keyboard.state[symbol]

    def on_update(self, dt):
        if not self.menu.show or self.first_update:
            self.world.process(dt)
            self.first_update = False
        self.menu.update(dt)

    def on_draw(self):
        arcade.start_render()

        arcade.set_viewport(64, 1280+64, -32, 720-32)
        draw_layers = [c for (_, c) in self.world.get_component(DrawLayer)]
        draw_layers.sort(key=lambda layer: layer.priority)
        for layer in draw_layers:
            layer.draw()

        for _, debug_circle in self.world.get_component(DebugCircle):
            if debug_circle.draw:
                arcade.draw_circle_filled(
                    debug_circle.x,
                    debug_circle.y,
                    debug_circle.size,
                    debug_circle.color
                )
        for _, debug in self.world.get_component(DebugPoly):
            if debug.draw:
                arcade.draw_polygon_outline(
                    debug.poly,
                    debug.color,
                    debug.size
                )
        
        arcade.set_viewport(0, 1280, 0, 720)
        for _, layer in self.world.get_component(HUDLayer):
            layer.draw()
        if self.menu.show:
            self.menu.draw()
        

