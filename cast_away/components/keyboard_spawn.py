
import arcade
import esper

from .input_source import KeyboardInputSource, START
from .spawner import PlayerSpawner
from .player import PlayerControlled

class KeyboardSpawnProcessor(esper.Processor):
    
    def is_started(self, input_source):
        for _, pc in self.world.get_component(PlayerControlled):
            if pc.input_source == input_source:
                return True
        return False

    def process(self, dt):
        for  _, input_source in self.world.get_component(KeyboardInputSource):
            name = input_source.name
            is_started = self.is_started(input_source)
            wants_to_start = input_source.state(START)
            if wants_to_start and not is_started:
                for  _, spawner in self.world.get_component(PlayerSpawner):
                    spawner.spawn(self.world, input_source)


def init(world):
    world.add_processor(KeyboardSpawnProcessor())