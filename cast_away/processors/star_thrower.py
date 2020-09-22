from cast_away.components.inventory import InventoryItem
import esper

from .. import keyboard

from cast_away.components.player import PlayerControlled
from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.timeout import Timeout
from cast_away.components.sprite import Sprite
from cast_away.components.player_bullet import PlayerBullet
from cast_away.components.input_source import WEAPON
from cast_away.components.star_thrower import StarThrower

class ShootingProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position, facing, item) in self.world.get_components(
            PlayerControlled, Position, Facing, InventoryItem
        ):
            if not self.world.has_component(item.ent, StarThrower):
                continue

            if self.world.has_component(item.ent, Timeout):
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
                self.world.add_component(item.ent, Timeout(.5))


def init(world):
    world.add_processor(ShootingProcessor())
