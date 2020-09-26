import esper
from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.sprite_effect import SpriteEffects, TwistEffect

class WalkProcessor(esper.Processor):
    def process(self, dt):
        for ent, (player, velocity) in self.world.get_components(Player, Velocity):
            if velocity.magnitude != 0:
                for sprite_effects in self.world.try_component(ent, SpriteEffects):
                    break
                else:
                    sprite_effects = SpriteEffects()
                    self.world.add_component(ent, sprite_effects)
                for effect in sprite_effects.effects:
                    if isinstance(effect, TwistEffect):
                        break
                else:
                    sprite_effects.effects.append(TwistEffect(
                        play_time=0.5, 
                        speed=2, 
                        size=.05
                    ))


def init(world):
    world.add_processor(WalkProcessor())