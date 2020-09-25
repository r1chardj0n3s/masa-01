import esper
import arcade

from cast_away.components.sound.music import Music, DEFAULT_MUSIC, MUSIC_VOLUME
from cast_away.components.timeout import Timeout


class MusicProcessor(esper.Processor):
    def __init__(self):
        self.music = None

    def process(self, dt):
        if self.music and self.music.is_complete():
            self.music = None
        for ent, music in self.world.get_component(Music):
            if self.world.has_component(ent, Timeout):
                continue
            self.music = arcade.Sound(music.file_path, streaming=True)
            self.music.play(MUSIC_VOLUME)
            self.world.delete_entity(ent)
        if self.music is None:
            self.world.create_entity(Music(DEFAULT_MUSIC))


def init(world):
    world.add_processor(MusicProcessor())
