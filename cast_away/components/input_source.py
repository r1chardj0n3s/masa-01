import arcade

from .. import keyboard

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
WEAPON = "weapon"
START = "start"
MENU = "menu"
ACTIVATE = "activate"
DROP = "drop"
SELECT_NEXT = "select next"
SELECT_PREV = "select prev"

class InputSource:
    def __init__(self, name, state):
        self.name = name
        self.state = state

_keybinds = {
    RIGHT: arcade.key.RIGHT,
    LEFT: arcade.key.LEFT,
    UP: arcade.key.UP,
    DOWN: arcade.key.DOWN,
    WEAPON: arcade.key.SPACE,
    MENU: arcade.key.ESCAPE,
    ACTIVATE: arcade.key.ENTER,
    DROP: arcade.key.Z,
    SELECT_NEXT: arcade.key.C,
    SELECT_PREV: arcade.key.X
}

class KeyboardState:
    def __init__(self):
        self.name = "keyboard"

    def get(self, action):
        return keyboard.state.get(_keybinds[action])


_buttonbinds = {
    WEAPON: 0,
    MENU: 7,
    ACTIVATE: 0,
    DROP: 1
    # SELECT_NEXT: arcade.key.BRACKETLEFT,
    # SELECT_PREV: arcade.key.BRACKETRIGHT
}

DEAD_ZONE_X = 0.1
DEAD_ZONE_Y = 0.1

class JoystickState:
    def __init__(self, joystick):
        self.joystick = joystick
        self.name = joystick.device.name
        self.buttons = dict()
        self.hat_x = 0
        self.hat_y = 0
        joystick.open()
        joystick.on_joybutton_press = self.on_joybutton_press
        joystick.on_joybutton_release = self.on_joybutton_release
        joystick.on_joyhat_motion = self.on_joyhat_motion

    def on_joybutton_press(self, _joystick, button):
        self.buttons[button] = True
        # print(f"button {button} press")

    def on_joybutton_release(self, _joystick, button):
        self.buttons[button] = False
        # print(f"button {button} release")

    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        self.hat_x = hat_x
        self.hat_y = hat_y

    def get(self, action):
        # print(f"joy.x {self.joystick.x}")
        # print(f"joy.y {self.joystick.y}")
        if action == LEFT:
            return self.joystick.x < DEAD_ZONE_X*-1
        elif action == RIGHT:
            return self.joystick.x > DEAD_ZONE_X
        elif action == UP:
            return self.joystick.y < DEAD_ZONE_Y*-1
        elif action == DOWN:
            return self.joystick.y > DEAD_ZONE_Y
        else:
            return self.buttons.get(_buttonbinds.get(action))