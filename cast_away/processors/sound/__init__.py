import esper
import arcade
from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.sound import Sound
from cast_away.components.timeout import Timeout

PLAYER_RUMBLE = ":resources:sounds/hit2.wav"


class SoundProcessor(esper.Processor):
    def __init__(self):
        self.rumble = arcade.Sound(PLAYER_RUMBLE, streaming=True)

    def process(self, dt):
        for ent, sound in self.world.get_component(Sound):
            if self.world.has_component(ent, Timeout):
                continue
            arcade_sound = arcade.Sound(sound.file_path)
            arcade_sound.play(volume=sound.volume)
            self.world.delete_entity(ent)

        for ent, (player, velocity) in self.world.get_components(Player, Velocity):
            if velocity.magnitude > 0:
                self.rumble.play(volume=0.002)
            else:
                self.rumble.stop()


def init(world):
    world.add_processor(SoundProcessor())
