import esper

from .. import keyboard

from cast_away.components.player import Player
from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.timeout import Timeout
from cast_away.components.sprite import Sprite
from cast_away.components.bullet import Bullet
from cast_away.components.input_source import ITEM_1
from cast_away.components.pickups import StarThrower
from cast_away.components.enemy import Enemy
from cast_away.components.inventory import InventoryItem
from cast_away.components.enemy import Enemy
from cast_away.components.collidable import Collidable, HitCircle

class ShootingProcessor(esper.Processor):
    def process(self, dt):
        for item_ent, (item, st) in self.world.get_components(InventoryItem, StarThrower):
            if self.world.has_component(item_ent, Timeout):
                continue

            pc = self.world.component_for_entity(item.owner_ent, Player)

            if pc.input_source.state.get(ITEM_1):
                position = self.world.component_for_entity(item.owner_ent, Position)
                facing = self.world.component_for_entity(item.owner_ent, Facing)
                velocity = facing.velocity()
                velocity.magnitude = 1000
                self.world.create_entity(
                    Sprite(":resources:images/items/star.png", scale=0.5),
                    Position(x=position.x, y=position.y, level=position.level),
                    velocity,
                    Bullet(.5, Enemy),
                    Collidable(match_components=[Enemy]),
                    HitCircle(radius=20)
                )
                self.world.add_component(item_ent, Timeout(0.5))


def init(world):
    world.add_processor(ShootingProcessor())
