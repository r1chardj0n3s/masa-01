from cast_away.components.graphics.emitter import Emitter
from cast_away.components.level import InLevel
from cast_away.components.draw_layer import DrawLayer, PARTICLE_LAYER


def create_particles(world, emitter_factory, position):
    emitter = emitter_factory(position)
    world.create_entity(
        Emitter(emitter), InLevel(position.level), DrawLayer(PARTICLE_LAYER, emitter)
    )
