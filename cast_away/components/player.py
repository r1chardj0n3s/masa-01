import arcade
import esper

from cast_away import keyboard

from .facing import Facing
from .velocity import Velocity


PLAYER_SPEED = 550
# kenney tiles have fake isometric, 2:1 pixel ratio of diagonals
# the following transformation ensures hitting the controller diagonally
# makes the character move on a "kenney-diagonal" line as drawn on the map
DIMETRIC_FACTOR = 5.0 ** 0.5  # sqrt(5) aka diagonal of a triangle with sides 2, 1 
PLAYER_SPEED_X = PLAYER_SPEED / DIMETRIC_FACTOR
PLAYER_SPEED_Y = PLAYER_SPEED / (DIMETRIC_FACTOR * 2)


class PlayerControlled:
    ...


class PlayerVelocityProcessor(esper.Processor):
    def process(self, dt):
        for _, (pc, velocity) in self.world.get_components(PlayerControlled, Velocity):
            dx = 0
            dy = 0
            if keyboard.state.get(arcade.key.UP):
                dy += PLAYER_SPEED_Y
            if keyboard.state.get(arcade.key.DOWN):
                dy -= PLAYER_SPEED_Y
            if keyboard.state.get(arcade.key.RIGHT):
                dx += PLAYER_SPEED_X
            if keyboard.state.get(arcade.key.LEFT):
                dx -= PLAYER_SPEED_X
            velocity.dx = dx
            velocity.dy = dy


class PlayerFacingProcessor(esper.Processor):
    def process(self, dt):
        for _, (pc, facing) in self.world.get_components(PlayerControlled, Facing):
            if keyboard.state.get(arcade.key.UP):
                facing.direction = Facing.NORTH
            if keyboard.state.get(arcade.key.DOWN):
                facing.direction = Facing.SOUTH
            if keyboard.state.get(arcade.key.RIGHT):
                facing.direction = Facing.EAST
            if keyboard.state.get(arcade.key.LEFT):
                facing.direction = Facing.WEST


def init(world):
    world.add_processor(PlayerVelocityProcessor())
    world.add_processor(PlayerFacingProcessor())
