import esper
from .sprite import Sprite

class SpriteEffect:
    def __init__(self, name, play_time, speed):
        self.play_time = play_time
        self.name = name
        self.speed = speed


class SpriteEffectProcessor(esper.Processor):

    def spin(self, dt, ent, sprite, effect):
        effect.play_time -= dt
        if effect.play_time < 0:
            sprite._arcade_sprite.angle = 0
            sprite._arcade_sprite.change_angle = 0
            self.world.remove_component(ent, SpriteEffect) 
        else:
            sprite._arcade_sprite.angle = sprite._arcade_sprite.angle + dt * effect.speed

    def process(self, dt):
        for ent, (sprite, effect) in self.world.get_components(
            Sprite, SpriteEffect
        ):
            if effect.name == "spin":
                self.spin(dt, ent, sprite, effect)


def init(world):
    world.add_processor(SpriteEffectProcessor())
