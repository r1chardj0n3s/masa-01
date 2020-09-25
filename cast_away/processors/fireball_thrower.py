import esper
import euclid
import random

from cast_away.components.player import Player
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.bullet import Bullet
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.fireball_thrower import FireballThrower
from cast_away.components.velocity import Velocity
from cast_away.components.sprite_effect import SpinEffect, SpriteEffects
from cast_away.components.facing import Facing


class FireballThrowerProcessor(esper.Processor):
    def process(self, dt):
        for thrower_ent, (thrower, thrower_pos) in self.world.get_components(FireballThrower, Position):
            thrower.timeout = max(0, thrower.timeout - dt)
            if thrower.timeout:
                continue

            choices = [pos for _, (p, pos) in self.world.get_components(Player, Position)]
            if not choices:
                continue

            if thrower.use_facing:
                facing = self.world.component_for_entity(thrower_ent, Facing)
                v = facing.velocity()
                v.magnitude = 250
            else:
                target_pos =  random.choice(choices)
                v = - target_pos.point2().connect(thrower_pos.point2()).v.normalize() * 250
                v = Velocity(v.x, v.y)

            self.world.create_entity(
                Sprite("data/kenney_platformerpack_redux/Particles/fireball.png", scale=0.5),
                Position(x=thrower_pos.x, y=thrower_pos.y, level=thrower_pos.level),
                v,
                Collidable(match_components=[Player]),
                HitCircle(radius=10),
                Bullet(1, Player),
                SpriteEffects(SpinEffect(play_time=1, speed=-400))
            )
            thrower.timeout = random.randint(1, 3)


def init(world):
    world.add_processor(FireballThrowerProcessor())
