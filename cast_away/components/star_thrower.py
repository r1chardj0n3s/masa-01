import arcade
import esper

from .. import keyboard

from .player import PlayerControlled
from .position import Position
from .facing import Facing
from .gun_cooldown import GunCooldown
from .sprite import Sprite
from .player_bullet import PlayerBullet
from .input_source import WEAPON

class ShootingProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position, facing) in self.world.get_components(
            PlayerControlled, Position, Facing
        ):
            if self.world.has_component(ent, GunCooldown):
                continue
            if pc.input_source.state(WEAPON):
                velocity = facing.velocity()
                velocity.magnitude = 1000
                self.world.create_entity(
                    Sprite(":resources:images/items/star.png", scale=0.5),
                    Position(x=position.x, y=position.y),
                    velocity,
                    PlayerBullet()
                )
                self.world.add_component(ent, GunCooldown(.5))


def init(world):
    world.add_processor(ShootingProcessor())
