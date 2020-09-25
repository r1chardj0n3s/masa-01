from dataclasses import dataclass, field
import arcade

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
MENU = "menu"
ACTIVATE = "activate"
ITEM_1 = "item 1"
ITEM_2 = "item 2"
ITEM_3 = "item 3"
DROP = "drop"
SELECT_NEXT = "select next"
SELECT_PREV = "select prev"


@dataclass
class InputEvent:
    input: str


@dataclass
class InputSource:
    name: str
    state: object


_keybinds = {
    RIGHT: arcade.key.RIGHT,
    LEFT: arcade.key.LEFT,
    UP: arcade.key.UP,
    DOWN: arcade.key.DOWN,
    MENU: arcade.key.ESCAPE,
    ACTIVATE: arcade.key.ENTER,
    ITEM_1: arcade.key.Z,
    ITEM_2: arcade.key.X,
    ITEM_3: arcade.key.C,
    DROP: arcade.key.LSHIFT,
}

KEYBOARD_MAP = dict((v, k) for k, v in _keybinds.items())


@dataclass
class KeyboardState:
    name: str = "keyboard"
    keys: object = field(default_factory=lambda: dict())
    events: object = field(default_factory=lambda: [])

    def update(self):
        pass

    def get(self, action):
        return self.keys.get(_keybinds[action])


# PS4 buttons:
# X = 1
# O = 2
# tri = 3
# LT = 4
# PS button = 12

_buttonbinds = {
    MENU: 7,
    ACTIVATE: 0,
    ITEM_1: 1,
    ITEM_2: 2,
    ITEM_3: 3,
    DROP: 4  # TODO PROBABLY NOT LEFT BUMPER
    # SELECT_NEXT: arcade.key.BRACKETLEFT,
    # SELECT_PREV: arcade.key.BRACKETRIGHT
}

_button_lookup = dict((v, k) for k, v in _buttonbinds.items())

DEAD_ZONE_X = 0.1
DEAD_ZONE_Y = 0.1


class JoystickState:
    def __init__(self, joystick):
        self.joystick = joystick
        self.name = joystick.device.name
        self.buttons = dict()
        self.events = []
        self.hat_x = 0
        self.hat_y = 0
        self.last_x = 0
        self.last_y = 0
        joystick.open()
        joystick.on_joybutton_press = self.on_joybutton_press
        joystick.on_joybutton_release = self.on_joybutton_release
        joystick.on_joyhat_motion = self.on_joyhat_motion

    def on_joybutton_press(self, _joystick, button):
        print(f"button {button} press")
        self.buttons[button] = True
        if button in _button_lookup:
            self.events.append(InputEvent(_button_lookup[button]))
        print(f"events: {self.events}")

    def on_joybutton_release(self, _joystick, button):
        self.buttons[button] = False
        # print(f"button {button} release")

    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        self.hat_x = hat_x
        self.hat_y = hat_y
        print(f"hat moved {hat_x} {hat_y}")

    def _joy_n(self, v, d):
        if v > d:
            return v
        if v < d * -1:
            return v
        return 0

    def _joy_x(self):
        return self._joy_n(self.joystick.x, DEAD_ZONE_X)

    def _joy_y(self):
        return self._joy_n(self.joystick.y, DEAD_ZONE_Y)

    def update(self):
        now_x = self._joy_x()
        if now_x < 0 and self.last_x >= 0:
            self.events.append(InputEvent(LEFT))
        if now_x > 0 and self.last_x <= 0:
            self.events.append(InputEvent(RIGHT))
        self.last_x = now_x

        now_y = self._joy_y()
        if now_y < 0 and self.last_y >= 0:
            self.events.append(InputEvent(UP))
        if now_y > 0 and self.last_y <= 0:
            self.events.append(InputEvent(DOWN))
        self.last_y = now_y

    def get(self, action):
        # print(f"joy.x {self.joystick.x}")
        # print(f"joy.y {self.joystick.y}")
        if action == LEFT:
            return self._joy_x() < 0
        elif action == RIGHT:
            return self._joy_x() > 0
        elif action == UP:
            return self._joy_y() < 0
        elif action == DOWN:
            return self._joy_y() > 0
        else:
            return self.buttons.get(_buttonbinds.get(action))
