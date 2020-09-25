import arcade

from cast_away.components.sprite import Sprite
from cast_away.components.sprite_effect import (
    AnimatedTextureEffect,
    SpriteEffects,
)
from cast_away.components.position import Position


def create_prop(world, x, y, type, level_ent):
    if type == "goat":
        sprite = [
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

    world.create_entity(
        *sprite,
        Position(x, y, level_ent),
    )
