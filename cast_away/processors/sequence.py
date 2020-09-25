import esper

from cast_away.components.sequence import Sequence
from cast_away.components.sprite_effect import SpriteEffects
from cast_away.components.timeout import Timeout


class SequenceProcessor(esper.Processor):
    def process(self, dt):
        for ent, sequence in self.world.get_component(Sequence):
            if isinstance(sequence.active_comp, SpriteEffects):
                if not sequence.active_comp.effects:
                    sequence.active_comp = None
            elif isinstance(sequence.active_comp, Timeout):
                if not sequence.active_comp.timeout:
                    sequence.active_comp = None
            else:
                sequence.active_comp = None

            if not sequence.active_comp:
                sequence.active_comp = sequence.comps.pop(0)
                self.world.add_component(sequence.target_ent, sequence.active_comp)

            if not sequence.comps:
                self.world.delete_entity(ent)


def init(world):
    world.add_processor(SequenceProcessor())
