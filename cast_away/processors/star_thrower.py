import arcade
import esper

from .. import keyboard

from cast_away.components.player import PlayerControlled
from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.gun_cooldown import GunCooldown
from cast_away.components.sprite import Sprite
from cast_away.components.player_bullet import PlayerBullet
from cast_away.components.input_source import WEAPON
from cast_away.components.star_thrower import StarThrower

class ShootingProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position, facing, st) in self.world.get_components(
            PlayerControlled, Position, Facing, StarThrower
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
