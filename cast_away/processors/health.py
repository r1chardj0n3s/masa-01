from cast_away.components.player import Player
import esper

from cast_away.components.invulnerable import Invulnerable
from cast_away.components.health import Health, HURT_SOUND
from cast_away.components.sprite_effect import SpriteEffects, SpinEffect, FlashEffect
from cast_away.event_dispatch import dispatch, Message, ENTITY_DIED
from cast_away.entities.sound import create_sound


class HealthProcessor(esper.Processor):
    def process(self, dt):
        for ent, health in self.world.get_component(Health):
            if health.amount < 3 and not health.effects:
                if health.regen_timeout:
                    health.regen_timeout -= dt
                    if health.regen_timeout < 0:
                        health.amount += 1
                        health.regen_timeout = 0
                else:
                    health.regen_timeout = 10

            for effect in list(health.effects):
                if not self.world.has_component(ent, Invulnerable):
                    health.amount -= effect.amount
                    if self.world.has_component(ent, Player):
                        self.world.add_component(ent, Invulnerable(1))
                    if not self.world.has_component(ent, SpriteEffects):
                        self.world.add_component(ent, SpriteEffects())
                    effects = self.world.component_for_entity(ent, SpriteEffects)
                    effects.effects.append(SpinEffect(play_time=0.3, speed=1000))
                    effects.effects.append(FlashEffect(play_time=1, speed=10000))
                    create_sound(self.world, HURT_SOUND, volume=0.5)
                health.effects.remove(effect)

            if health.amount <= 0:
                dispatch(self.world, ENTITY_DIED, ent)


def init(world):
    world.add_processor(HealthProcessor())
