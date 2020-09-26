import esper

from cast_away.components.facing import Facing
from cast_away.components.velocity import Velocity
from cast_away.components.input_source import LEFT, RIGHT, UP, DOWN
from cast_away.components.player import Player
from cast_away.components.sprite_effect import SpriteEffects, TwistEffect

PLAYER_SPEED = 200
PLAYER_ACCEL = 60
PLAYER_DECEL = 1.3
DEAD_ZONE_X = 10
DEAD_ZONE_Y = 10

def process_velocity(initial, vector, dead, maximum):
    final = (initial + vector) / PLAYER_DECEL
    if abs(final) < dead:
        return 0
    if final > maximum:
        return maximum
    if final < maximum * -1:
        return maximum * -1
    return final

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
            vector = Velocity(0,0)
            if left_right or up_down:
                facing.set_cardinals(left_right, up_down)
                vector = facing.velocity()
                vector.magnitude = PLAYER_ACCEL

            velocity.dx = process_velocity(velocity.dx, vector.dx, DEAD_ZONE_X, PLAYER_SPEED)
            velocity.dy = process_velocity(velocity.dy, vector.dy, DEAD_ZONE_Y, PLAYER_SPEED)
            # velocity.magnitude = PLAYER_SPEED if left_right or up_down else 0
            self.world.add_component(ent, velocity)


def init(world):
    world.add_processor(PlayerVelocityProcessor())
