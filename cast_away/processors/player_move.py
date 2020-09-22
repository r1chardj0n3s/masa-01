import esper

from cast_away.components.facing import Facing
from cast_away.components.velocity import Velocity
from cast_away.components.input_source import LEFT, RIGHT, UP, DOWN
from cast_away.components.player import Player

PLAYER_SPEED = 250


class PlayerVelocityProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, velocity, facing) in self.world.get_components(
            Player, Velocity, Facing
        ):
            input_source = pc.input_source
            left_right = up_down = 0
            if input_source.state.get(RIGHT):
                left_right = 1
            if input_source.state.get(LEFT):
                left_right -= 1
            if input_source.state.get(UP):
                up_down = 1
            if input_source.state.get(DOWN):
                up_down -= 1
            if left_right or up_down:
                facing.set_cardinals(left_right, up_down)

            velocity = facing.velocity()
            velocity.magnitude = PLAYER_SPEED if left_right or up_down else 0
            self.world.add_component(ent, velocity)


def init(world):
    world.add_processor(PlayerVelocityProcessor())
