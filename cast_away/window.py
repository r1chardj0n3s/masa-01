import arcade


from . import keyboard
from .processors import init_world
from .components.draw_layer import DrawLayer
from .components.debug_primitives import DebugCircle, DebugPoly
from .components.collidable import HitCircle, HitPoly
from .components.position import Position
from .components.level import CurrentLevel, Level
from .components.level.arena_boundary import ArenaBoundary
from .components.input_source import InputSource, KeyboardState

from .menu import Menu
from cast_away.components.hud.hud_layer import HUDLayer

class Game(arcade.Window):
    def __init__(self, map_name="1-movement"):
        super().__init__(1280, 720, "Junk Yard Wars")
        self.world = init_world()
        self.world.create_entity(InputSource("Keyboard", KeyboardState()))
        self.world.create_entity(CurrentLevel(next_level = map_name))
        self.menu = Menu(self, self.world)
        self.first_update = True

    def on_key_press(self, symbol, modifiers):
        keyboard.state[symbol] = True

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
        draw_layers = [c for (_, c) in self.world.get_component(DrawLayer)]
        draw_layers.sort(key=lambda layer: layer.priority)
        for layer in draw_layers:
            layer.draw()

        for _, (position, hitCircle) in self.world.get_components(Position, HitCircle):
            if position.level is not None:
                level = self.world.component_for_entity(position.level, Level)
                if level.loaded:
                    arcade.draw_circle_filled(
                        position.x,
                        position.y,
                        hitCircle.radius,
                        (255,0,0,100)
                    )
        for _, (position, hitPoly) in self.world.get_components(Position, HitPoly):
            level = self.world.component_for_entity(position.level, Level)
            if level.loaded:
                arcade.draw_polygon_outline(
                    hitPoly.point_list,
                    (255,255,255,100),
                    5
                )

        for _, boundary in self.world.get_component(ArenaBoundary):
            arcade.draw_polygon_outline(
                boundary.poly.point_list,
                arcade.color.WHITE,
                5
            )
        
        arcade.set_viewport(0, 1280, 0, 720)
        for _, layer in self.world.get_component(HUDLayer):
            layer.draw()
        if self.menu.show:
            self.menu.draw()
