import esper

from cast_away.components.position import Position
from cast_away.components.velocity import Velocity, BounceVelocityBack


class VelocityEffectProcessor(esper.Processor):
    def process(self, dt):
        for bounce_ent, (bounce) in self.world.get_component(BounceVelocityBack):
            target_ent = bounce.target_ent
            velocity = self.world.component_for_entity(target_ent, Velocity)
            position = self.world.component_for_entity(target_ent, Position)
            position.x -= velocity.dx * dt * bounce.magnitude
            position.y -= velocity.dy * dt * bounce.magnitude
            self.world.delete_entity(bounce_ent)


def init(world):
    world.add_processor(VelocityEffectProcessor())
