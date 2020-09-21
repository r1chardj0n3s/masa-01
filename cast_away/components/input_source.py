from .. import keyboard
import arcade

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"
WEAPON = "weapon"

_keybinds = {
    RIGHT: arcade.key.RIGHT,
    LEFT: arcade.key.LEFT,
    UP: arcade.key.UP,
    DOWN: arcade.key.DOWN,
    WEAPON: arcade.key.SPACE,
}

class KeyboardInputSource:
    def state(self, action):
        return keyboard.state.get(_keybinds[action])
