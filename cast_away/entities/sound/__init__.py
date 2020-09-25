from cast_away.components.sound import Sound
from cast_away.components.timeout import Timeout

def create_sound(world, file_path, volume=0.05, delay=None):
    ent = world.create_entity(Sound(file_path, volume))
    if delay is not None:
        world.add_component(ent, Timeout(delay))