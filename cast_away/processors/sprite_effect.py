import esper

from cast_away.components.sprite import Sprite
from cast_away.components.sprite_effect import SpriteEffects

class SpriteEffectProcessor(esper.Processor):
    def process(self, dt):
        for ent, (sprite, effects) in self.world.get_components(Sprite, SpriteEffects):
            for effect in list(effects.effects):
                effect.play_time -= dt
                if effect.play_time < 0:
                    effect.run(0, sprite)
                    effect.clear(sprite)
                    effects.effects.remove(effect)
                    if not effects.effects:
                        self.world.remove_component(ent, SpriteEffects)
                else:
                    effect.run(dt, sprite)


def init(world):
    world.add_processor(SpriteEffectProcessor())
