import esper

from cast_away.components.position import Position
from cast_away.components.position_effects import PositionEffects

class PositionEffectProcessor(esper.Processor):
    def process(self, dt):
        for ent, (position, effects) in self.world.get_components(Position, PositionEffects):
            for effect in list(effects.effects):
                effect.play_time -= dt
                if effect.play_time < 0:
                    effect.run(0, position)
                    effect.clear(position)
                    effects.effects.remove(effect)
                    if not effects.effects:
                        self.world.remove_component(ent, PositionEffects)
                else:
                    effect.run(dt, position)


def init(world):
    world.add_processor(PositionEffectProcessor())
