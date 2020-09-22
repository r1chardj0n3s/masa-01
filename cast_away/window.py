import arcade

import arcade.gui
from arcade.gui import UIFlatButton, UIGhostFlatButton, UIManager
from arcade.gui.ui_style import UIStyle

from . import keyboard
from .processors import init_world
from .components.draw_layer import DrawLayer
from .components.debug_primitives import DebugCircle, DebugPoly
from .components.level import CurrentLevel
from .components.input_source import KeyboardInputSource

from .hud import add_health_hud

class Game(arcade.Window):
    def __init__(self, map_name="1-movement"):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()
        self.world.create_entity(KeyboardInputSource())
        self.world.create_entity(CurrentLevel(map_name))
        add_health_hud(self.world)
        self.paused = True
        self.menu = Menu(self, self.world)

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True
        if symbol == arcade.key.ESCAPE:
            self.paused = not self.paused

    def on_key_release(self, symbol, modifiers):
        del keyboard.state[symbol]

    def on_update(self, dt):
        if not self.paused:
            self.world.process(dt)
        else:
            self.menu.update(dt)

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
        
        if self.paused:
            self.menu.draw()
        

class Menu:
    def __init__(self, window, world):
        self.window = window
        self.world = world
    
        self.ui_manager = UIManager(self.window)
        
        def style(button):
            button.set_style_attrs(
                font_color=arcade.color.WHITE,
                font_color_hover=arcade.color.WHITE,
                font_color_press=arcade.color.WHITE,
                bg_color=(51, 139, 57),
                bg_color_hover=(51, 139, 57),
                bg_color_press=(28, 71, 32),
                border_color=(51, 139, 57),
                border_color_hover=arcade.color.WHITE,
                border_color_press=arcade.color.WHITE
            )
        self.start = UIFlatButton('Play', center_x=self.window.width/2, center_y=self.window.height/2, width=200, height=40)
        style(self.start)
        self.ui_manager.add_ui_element(self.start)
        self.exit = UIFlatButton('Exit', center_x=self.window.width/2, center_y=self.window.height/2-50, width=200, height=40)
        style(self.exit)
        self.ui_manager.add_ui_element(self.exit)

    def update(self, dt):
        if self.start.pressed:
            self.window.paused = False
        if self.exit.pressed:
            arcade.close_window()

    def draw(self):
        self.ui_manager.on_draw()
