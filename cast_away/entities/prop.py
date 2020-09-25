import arcade

from cast_away.components.sprite import Sprite
from cast_away.components.sprite_effect import AnimatedTextureEffect, FadeEffect, SpriteEffects
from cast_away.components.position import Position
from cast_away.components.timeout import Timeout
from cast_away.components.sequence import Sequence


def create_prop(world, x, y, type, level_ent):
    if type == "goat":git 
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

    elif type == "dialog-1":
        sprite = [
            Sprite("data/images/dialog-1.png"),
        ]

    ent = world.create_entity(
        *sprite,
        Position(x, y, level_ent),
    )

    if type == "dialog-1":
        world.create_entity(Sequence(ent, Timeout(5), SpriteEffects(FadeEffect(.5))))
