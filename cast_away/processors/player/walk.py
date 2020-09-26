import esper
import arcade
from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.sprite_effect import SpriteEffects, TwistEffect


PLAYER_WALK_SOUND = "data/sound/Castaway_move_3.wav"

class WalkProcessor(esper.Processor):
    def __init__(self):
        self.walk_sound = arcade.Sound(PLAYER_WALK_SOUND)
        self.walk_sound.play(volume=0)

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
                        play_time=0.2, 
                        size=.005
                    ))

                if not self.walk_sound.is_complete() == 0:
                    self.walk_sound.play(volume=0.1)
            else:
                self.walk_sound.stop()


def init(world):
    world.add_processor(WalkProcessor())