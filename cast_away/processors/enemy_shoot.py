import esper
import euclid
import random

from cast_away.components.player import Player
from cast_away.components.position import Position
from cast_away.components.timeout import Timeout
from cast_away.components.sprite import Sprite
from cast_away.components.bullet import Bullet
from cast_away.components.fireball_thrower import FireballThrower
from cast_away.components.enemy import Enemy
from cast_away.components.velocity import Velocity
from cast_away.components.sprite_effect import SpinEffect, SpriteEffects


class EnemyShootingProcessor(esper.Processor):
    def process(self, dt):
        for _, (thrower, thrower_pos) in self.world.get_components(FireballThrower, Position):
            thrower.timeout = max(0, thrower.timeout - dt)
            if thrower.timeout:
                continue

            choices = [pos for _, (p, pos) in self.world.get_components(Player, Position)]
            if not choices:
                continue

            target_pos =  random.choice(choices)
            v = - target_pos.point2().connect(thrower_pos.point2()).v.normalize() * 250

            self.world.create_entity(
                Sprite("data/kenney_platformerpack_redux/Particles/fireball.png", scale=0.5),
                Position(x=thrower_pos.x, y=thrower_pos.y),
                Velocity(v.x, v.y),
                Bullet(1, Player),
                SpriteEffects(SpinEffect(play_time=1, speed=-400))
            )
            thrower.timeout = random.randint(1, 3)


def init(world):
    world.add_processor(EnemyShootingProcessor())
