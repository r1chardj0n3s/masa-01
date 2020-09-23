import arcade
import random
from dataclasses import dataclass

from cast_away.components.sprite import Sprite, SpriteList
from cast_away.components.facing import Facing


COLOURS = "blue green yellow red".split()


@dataclass
class MultiplayerIdentifier:
    colour: str

    @classmethod
    def select(cls, others):
        if len(others) == len(COLOURS):
            cls(random.choice(COLOURS))
        return cls(
            random.choice(list(set(COLOURS) - set(other.colour for other in others)))
        )


def player_sprite_for(colour, facing):
    s = Sprite("data/kenney_robot-pack_side/robot_blueDrive1.png", scale=0.25)
    s._arcade_sprite.texture = player_texture_for(colour, facing)
    return s


def player_texture_for(colour, facing):
    if facing in (Facing.NORTH, Facing.NORTH_EAST):
        return arcade.load_texture(
            f"data/kenney_robot-pack_side/robot_{colour}Drive1 - Butt.png"
        )
    elif facing in (Facing.EAST, Facing.SOUTH_EAST, Facing.NEUTRAL):
        return arcade.load_texture(
            f"data/kenney_robot-pack_side/robot_{colour}Drive1.png"
        )
    elif facing in (Facing.SOUTH, Facing.SOUTH_WEST):
        return arcade.load_texture(
            f"data/kenney_robot-pack_side/robot_{colour}Drive1.png",
            flipped_horizontally=True,
        )
    elif facing in (Facing.WEST, Facing.NORTH_WEST):
        return arcade.load_texture(
            f"data/kenney_robot-pack_side/robot_{colour}Drive1 - Butt.png",
            flipped_horizontally=True,
        )
