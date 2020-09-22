import esper
from .sprite import Sprite

class SpriteEffects:
    def __init__(self, *effects):
        self.effects = list(effects)

class SpinEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.initial_angle = None
    
    def clear(self, sprite):
        sprite._arcade_sprite.angle = self.initial_angle

    def run(self, dt, sprite):
        a_sprite = sprite._arcade_sprite
        if self.initial_angle is None:
            self.initial_angle = a_sprite.angle
        a_sprite.angle = a_sprite.angle + dt * self.speed

class FlashEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.direction = -1
        self.initial_alpha = None
    
    def clear(self, sprite):
        sprite._arcade_sprite.alpha = self.initial_alpha

    def run(self, dt, sprite):
        a_sprite = sprite._arcade_sprite
        self.last_alpha = a_sprite.alpha
        if self.initial_alpha is None:
            self.initial_alpha = self.last_alpha
        new_alpha = self.last_alpha - self.direction*self.speed*dt
        if new_alpha < 0:
            new_alpha = 0
            self.direction *= -1
        elif new_alpha > 255:
            new_alpha = 255
            self.direction *= -1
        a_sprite.alpha = new_alpha

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
