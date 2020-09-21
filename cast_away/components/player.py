import arcade
import esper

from cast_away import keyboard

from .facing import Facing
from .velocity import Velocity
from .sprite import Sprite


PLAYER_SPEED = 550


class PlayerControlled:
    ...


class PlayerVelocityProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, velocity, facing) in self.world.get_components(PlayerControlled, Velocity, Facing):
            left_right = up_down = 0
            if keyboard.state.get(arcade.key.RIGHT):
                left_right = 1
            if keyboard.state.get(arcade.key.LEFT):
                left_right -= 1
            if keyboard.state.get(arcade.key.UP):
                up_down = 1
            if keyboard.state.get(arcade.key.DOWN):
                up_down -= 1
            facing.set_cardinals(left_right, up_down)

            velocity = facing.velocity()
            velocity.magnitude = PLAYER_SPEED
            self.world.add_component(ent, velocity)


def init(world):
    world.add_processor(PlayerVelocityProcessor())
