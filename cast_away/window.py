import arcade

from . import keyboard
from .components import init_world
from .components.draw_layer import DrawLayer
from .components.debug_primitives import DebugCircle, DebugPoly
from .components.level import CurrentLevel


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()
        self.world.create_entity(CurrentLevel("1-movement"))

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
        del keyboard.state[symbol]

    def on_update(self, dt):
        self.world.process(dt)

    def on_draw(self):
        arcade.start_render()
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
