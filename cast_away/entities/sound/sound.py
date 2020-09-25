from cast_away.components.sound import Sound

def play_sound(world, file_path):
    world.create_entity(Sound(file_path))