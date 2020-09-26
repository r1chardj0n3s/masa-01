import esper
import random

from cast_away.components.player import Player
from cast_away.components.position import Position
from cast_away.components.sprite import Sprite
from cast_away.components.bullet import Bullet
from cast_away.components.collidable import Collidable, HitCircle
from cast_away.components.fireball_thrower import (
    FireballThrower,
    FIREBALL_IMAGE,
    FIREBALL_SHOOT_SOUND,
)
from cast_away.components.velocity import Velocity
from cast_away.components.sprite_effect import SpinEffect, SpriteEffects
from cast_away.components.facing import Facing
from cast_away.components.level import Level
from cast_away.components.hit_emitter import HitEmitter
from cast_away.entities.sound import create_sound
from cast_away.graphics.emitters import smoke_poof


class FireballThrowerProcessor(esper.Processor):
    def process(self, dt):
        for thrower_ent, (thrower, thrower_pos) in self.world.get_components(
            FireballThrower, Position
        ):
            level = self.world.component_for_entity(thrower_pos.level, Level)
            if not level.active:
                continue

            thrower.timeout = max(0, thrower.timeout - dt)
            if thrower.timeout:
                continue

            choices = [
                pos for _, (p, pos) in self.world.get_components(Player, Position)
            ]
            if not choices:
                continue

            if thrower.use_facing:
                facing = self.world.component_for_entity(thrower_ent, Facing)
                v = facing.velocity()
                v.magnitude = 250
            else:
                target_pos = random.choice(choices)
                v = (
                    -target_pos.point2().connect(thrower_pos.point2()).v.normalize()
                    * 250
                )
                v = Velocity(v.x, v.y)

            self.world.create_entity(
                Sprite(FIREBALL_IMAGE, scale=0.5),
                Position(x=thrower_pos.x, y=thrower_pos.y, level=thrower_pos.level),
                v,
                Collidable(match_components=[Player]),
                HitCircle(radius=10),
                Bullet(1, Player),
                SpriteEffects(SpinEffect(play_time=1, speed=-800)),
                HitEmitter(smoke_poof)
            )
            create_sound(self.world, FIREBALL_SHOOT_SOUND)
            thrower.timeout = random.randint(1, 3)


def init(world):
    world.add_processor(FireballThrowerProcessor())
