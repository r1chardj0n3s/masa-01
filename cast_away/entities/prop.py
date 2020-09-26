import arcade

from cast_away.components.prop import Prop
from cast_away.components.sprite import Sprite
from cast_away.components.sprite_effect import (
    AnimatedTextureEffect,
    SpriteEffects,
)
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitCircle


def create_prop(world, x, y, type, radius, level_ent):
    if type == "goat":
        comps = [
            Sprite("data/images/goat-1.png"),
            SpriteEffects(
                AnimatedTextureEffect(
                    [
                        (5, arcade.load_texture("data/images/goat-1.png")),
                        (0.05, arcade.load_texture("data/images/goat-2.png")),
                        (0.05, arcade.load_texture("data/images/goat-3.png")),
                        (0.5, arcade.load_texture("data/images/goat-4.png")),
                        (0.05, arcade.load_texture("data/images/goat-3.png")),
                        (0.05, arcade.load_texture("data/images/goat-2.png")),
                    ]
                )
            ),
        ]

    if radius:
        comps.extend([Collidable(), HitCircle(radius)])

    world.create_entity(
        Prop(type),
        *comps,
        Position(x, y, level_ent),
    )
