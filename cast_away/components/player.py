import esper

from cast_away import keyboard

from .facing import Facing
from .velocity import Velocity
from .sprite import Sprite
from .input_source import LEFT, RIGHT, UP, DOWN

PLAYER_SPEED = 550

class PlayerControlled:
    def __init__(self, input_source):
        self.input_source = input_source


class PlayerVelocityProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, velocity, facing) in self.world.get_components(PlayerControlled, Velocity, Facing):
            input_source = pc.input_source
            left_right = up_down = 0
            if input_source.state(RIGHT):
                left_right = 1
            if input_source.state(LEFT):
                left_right -= 1
            if input_source.state(UP):
                up_down = 1
            if input_source.state(DOWN):
                up_down -= 1
            if left_right or up_down:
                facing.set_cardinals(left_right, up_down)

            velocity = facing.velocity()
            velocity.magnitude = PLAYER_SPEED if left_right or up_down else 0
            self.world.add_component(ent, velocity)


def init(world):
    world.add_processor(PlayerVelocityProcessor())
