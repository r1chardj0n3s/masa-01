import arcade

from .. import keyboard

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
WEAPON = "weapon"
START = "start"

_keybinds = {
    RIGHT: arcade.key.RIGHT,
    LEFT: arcade.key.LEFT,
    UP: arcade.key.UP,
    DOWN: arcade.key.DOWN,
    WEAPON: arcade.key.SPACE,
}

class KeyboardInputSource:
    def __init__(self):
        ...

    def state(self, action):
        return keyboard.state.get(_keybinds[action])


_buttonbinds = {
    WEAPON: 0,
    START: 7,
}

DEAD_ZONE_X = 0.1
DEAD_ZONE_Y = 0.1

class JoystickInputSource:
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
        # print(f"button {button} down")

    def on_joybutton_release(self, _joystick, button):
        self.buttons[button] = False

    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        self.hat_x = hat_x
        self.hat_y = hat_y

    def state(self, action):
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