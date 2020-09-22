import arcade
import arcade.gui
from arcade.gui import UIFlatButton, UIManager
from .components.input_source import (
    InputSource,
    JoystickState,
    KeyboardState,
    MENU,
    UP,
    DOWN,
    ACTIVATE,
)
from .components.player import Player
from .components.level import CurrentLevel
from .components.spawner import PlayerSpawner
from .components.position import Position
from .entities import player

# from arcade.gui.ui_style import UIStyle
MENU_SPEED = 0.1
JOYSTICK_CHECK_FREQUENCY = 5

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10

START = "Play"
EXIT = "Exit"
BUTTONS = [START, EXIT]


def check_joysticks(world):
    all_joysticks = []
    for _, input_source in world.get_component(InputSource):
        all_joysticks.append(input_source.name)
    # arcade.get_joysticks is a time consuming operation and will skip frames
    joysticks = arcade.get_joysticks()
    if joysticks:
        for joystick in joysticks:
            name = joystick.device.name
            if name not in all_joysticks:
                print("new joystick! {name}")
                world.create_entity(InputSource(name, JoystickState(joystick)))
                all_joysticks.append(name)
        # TODO: clean up removed joysticks


class Menu:
    def __init__(self, window, world):
        self.window = window
        self.world = world
        self.menu_input = 0
        self.joystick_check = JOYSTICK_CHECK_FREQUENCY
        self.selected_button = None
        self.show = True

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
                border_color_press=arcade.color.WHITE,
            )

        half_width = self.window.width / 2
        half_height = self.window.height / 2
        panel_height = len(BUTTONS) * (BUTTON_HEIGHT + BUTTON_MARGIN)
        half_panel_height = panel_height / 2

        def button(num, name):
            offset_y = half_panel_height - (BUTTON_HEIGHT + BUTTON_MARGIN) * num
            b = UIFlatButton(
                name,
                center_x=half_width,
                center_y=half_height + offset_y,
                width=BUTTON_WIDTH,
                height=BUTTON_HEIGHT,
            )
            style(b)
            self.ui_manager.add_ui_element(b)
            return b

        self.buttons = {}
        for num, name in enumerate(BUTTONS):
            self.buttons[name] = button(num, name)

    def highlight_button(self, direction):
        button_count = len(BUTTONS)
        first_button = 0
        last_button = button_count - 1
        if self.selected_button is None:
            if direction > 0:
                self.selected_button = first_button
            else:
                self.selected_button = last_button
        else:
            self.selected_button += direction
            if self.selected_button < 0:
                self.selected_button = last_button
            if self.selected_button == button_count:
                self.selected_button = first_button
        for i, name in enumerate(BUTTONS):
            button = self.buttons[name]
            button.hovered = i == self.selected_button

    def update(self, dt):
        for _, input_source in self.world.get_component(InputSource):
            if input_source.state.get(MENU):
                self.show = True
        if self.show:
            self.joystick_check += dt
            menu_activator = None
            if self.joystick_check > JOYSTICK_CHECK_FREQUENCY:
                check_joysticks(self.world)
                self.joystick_check = 0

            self.menu_input -= dt
            if self.menu_input < 0:
                for _, input_source in self.world.get_component(InputSource):
                    if input_source.state.get(DOWN):
                        self.highlight_button(1)
                        self.menu_input = MENU_SPEED
                    if input_source.state.get(UP):
                        self.highlight_button(-1)
                        self.menu_input = MENU_SPEED
                    if (
                        input_source.state.get(ACTIVATE)
                        and self.selected_button is not None
                    ):
                        self.buttons[BUTTONS[self.selected_button]].pressed = True
                        menu_activator = input_source
                        self.menu_input = MENU_SPEED

            if self.buttons[START].pressed:
                self.show = False
                if menu_activator == None:
                    for _, input_source in self.world.get_component(InputSource):
                        if input_source.name == "Keyboard":
                            menu_activator = input_source
                self.spawn_player(menu_activator)
                self.buttons[START].pressed = False
            if self.buttons[EXIT].pressed:
                arcade.close_window()

    def draw(self):
        self.ui_manager.on_draw()

    def is_started(self, input_source):
        for _, pc in self.world.get_component(Player):
            if pc.input_source == input_source:
                return True
        return False

    def spawn_player(self, input_source):
        name = input_source.name
        is_started = self.is_started(input_source)
        if not is_started:
            for _, current_level in self.world.get_component(CurrentLevel):
                for _, (spawner, position) in self.world.get_components(
                    PlayerSpawner, Position
                ):
                    if spawner.last_level == current_level.last_level:
                        player.create_player(self.world, position, input_source)
                        break
                else:
                    # just go with the first spawn (prolly a dev loading straight in)
                    for _, (spawner, position) in self.world.get_components(
                        PlayerSpawner, Position
                    ):
                        player.create_player(self.world, position, input_source)
                        break