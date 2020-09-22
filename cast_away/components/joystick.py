
import arcade
import esper

from .input_source import JoystickInputSource, START
from .spawner import PlayerSpawner
from .player import PlayerControlled
from .level import CurrentLevel
from .. import keyboard

CHECK_FREQUENCY = 1

class JoystickDetectionProcessor(esper.Processor):
    def __init__(self):
        self.counter = 0
    
    def is_started(self, input_source):
        for _, pc in self.world.get_component(PlayerControlled):
            if pc.input_source == input_source:
                return True
        return False

    def process(self, dt):
        self.counter += dt
        if self.counter < CHECK_FREQUENCY:
            return
        self.counter = 0
        all_joysticks = []
        for  _, input_source in self.world.get_component(JoystickInputSource):
            name = input_source.name
            all_joysticks.append(name)
            is_started = self.is_started(input_source)
            wants_to_start = input_source.state(START)
            # print(f"joystick {name} is started {is_started} wants to start {wants_to_start}")
            if wants_to_start and not is_started:
                for  _, current_level in self.world.get_component(CurrentLevel):
                    for  _, spawner in self.world.get_component(PlayerSpawner):
                        if spawner.last_level == current_level.last_level:
                            spawner.spawn(self.world, input_source)
        #arcade.get_joysticks is a time consuming operation and will skip frames
        if not keyboard.state.get(arcade.key.J):
            return
        joysticks = arcade.get_joysticks()
        if joysticks:
            for joystick in joysticks:
                name = joystick.device.name
                if name not in all_joysticks:
                    print("new joystick! {name}")
                    self.world.create_entity(JoystickInputSource(joystick))
                    all_joysticks.append(name)
            #TODO: clean up removed joysticks


def init(world):
    world.add_processor(JoystickDetectionProcessor())