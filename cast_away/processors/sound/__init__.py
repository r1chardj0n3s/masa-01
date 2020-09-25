import esper
import arcade

from cast_away.components.sound import Sound
from cast_away.components.timeout import Timeout


class SoundProcessor(esper.Processor):
    def process(self, dt):
        for ent, sound in self.world.get_component(Sound):
            if self.world.has_component(ent, Timeout):
                continue
            arcade_sound = arcade.Sound(sound.file_path)
            arcade_sound.play(volume=sound.volume)
            self.world.delete_entity(ent)


def init(world):
    world.add_processor(SoundProcessor())
