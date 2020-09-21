import esper
from .sprite import Sprite

class SpriteEffects:
    def __init__(self):
        self.effects = []

class SpinEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
    
    def clear(self, sprite):
        sprite._arcade_sprite.angle = 0
        sprite._arcade_sprite.change_angle = 0

    def run(self, dt, sprite):
        a_sprite = sprite._arcade_sprite
        a_sprite.angle = a_sprite.angle + dt * self.speed


class SpriteEffectProcessor(esper.Processor):
    def process(self, dt):
        for ent, (sprite, effects) in self.world.get_components(Sprite, SpriteEffects):
            for effect in list(effects.effects):
                effect.play_time -= dt
                if effect.play_time < 0:
                    effect.clear(sprite)
                    effects.effects.remove(effect)
                else:
                    effect.run(dt, sprite)


def init(world):
    world.add_processor(SpriteEffectProcessor())
