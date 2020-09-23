import arcade
import esper

from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.sprite import Sprite, SpriteList
from cast_away.components.multiplayer_identifier import MultiplayerIdentifier, player_texture_for


class SpriteProcessor(esper.Processor):
    def process(self, dt):
        for _, (sprite, position) in self.world.get_components(Sprite, Position):
            sprite._arcade_sprite.center_x = position.x
            sprite._arcade_sprite.center_y = position.y


# make the arcade sprite list (a singleton, hopefully) reflect the ECS sprites
class SpriteListProcessor(esper.Processor):
    def process(self, dt):
        all_sprites = set(sprite for _, sprite in self.world.get_component(Sprite))

        for _, sprite_list in self.world.get_component(SpriteList):
            for sprite in list(sprite_list._arcade_sprite_list):
                if sprite not in all_sprites:
                    sprite_list._arcade_sprite_list.remove(sprite)

            for sprite in all_sprites:
                if (
                    sprite._arcade_sprite
                    not in sprite_list._arcade_sprite_list.sprite_list
                ):
                    sprite_list._arcade_sprite_list.append(sprite._arcade_sprite)


def init(world):
    world.add_processor(SpriteProcessor())
    world.add_processor(SpriteListProcessor())


class SpriteFacingProcessor(esper.Processor):
    def process(self, dt):
        for _, (mp, sprite, facing) in self.world.get_components(
            MultiplayerIdentifier, Sprite, Facing
        ):
            sprite._arcade_sprite.texture = player_texture_for(mp.colour, facing.direction)


def init(world):
    world.add_processor(SpriteProcessor())
    world.add_processor(SpriteListProcessor())
    world.add_processor(SpriteFacingProcessor())
