import esper

from cast_away.components.graphics.emitter import Emitter


class EmitterProcessor(esper.Processor):
    def process(self, dt):
        for ent, emitter in self.world.get_component(Emitter):
            emitter._arcade_emitter.update()
            if emitter._arcade_emitter.can_reap():
                self.world.delete_entity(ent)


def init(world):
    world.add_processor(EmitterProcessor())
