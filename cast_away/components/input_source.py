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
    def __init__(self):
        ...
        
    def state(self, action):
        return keyboard.state.get(_keybinds[action])


# class JoystickInputSource:
#     def __init__(self, joystick):
#         self.joystick = joystick

#     def state(self, action):
#         return 

# class JoystickDetectionProcessor(esper.Processor):
    
#     def process(self, dt):
#         joysticks = arcade.get_joysticks()
#         if joysticks:
#             for joystick in joysticks:

#                 self.joystick.open()
#                 self.joystick.on_joybutton_press = self.on_joybutton_press
#                 self.joystick.on_joybutton_release = self.on_joybutton_release
#                 self.joystick.on_joyhat_motion = self.on_joyhat_motion