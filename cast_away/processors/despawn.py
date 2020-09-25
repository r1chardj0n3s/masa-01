import esper
from cast_away.components.despawn import Despawn
from cast_away.components.sprite_effect import SpriteEffects, FlashEffect


class DespawnProcessor(esper.Processor):
    def process(self, dt):
        for ent, despawn in self.world.get_component(Despawn):
            despawn.after_time -= dt
            if despawn.after_time < 1 and not despawn.effect_playing:
                despawn.effect_playing = True
                self.world.add_component(ent, SpriteEffects(FlashEffect(1, 10000)))
            if despawn.after_time > 0:
                continue
            self.world.delete_entity(ent)


def init(world):
    world.add_processor(DespawnProcessor())
