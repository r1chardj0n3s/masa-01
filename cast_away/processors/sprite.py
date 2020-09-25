import arcade
import esper

from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.sprite import Sprite, SpriteList
from cast_away.components.level import InLevel
from cast_away.components.multiplayer_identifier import (
    MultiplayerIdentifier,
    player_texture_for,
)
from cast_away.components.draw_layer import DrawLayer


class SpriteProcessor(esper.Processor):
    def process(self, dt):
        for _, (sprite, position) in self.world.get_components(Sprite, Position):
            sprite._arcade_sprite.center_x = position.x
            sprite._arcade_sprite.center_y = position.y


# make the arcade sprite list (a singleton, hopefully) reflect the ECS sprites
class SpriteListProcessor(esper.Processor):
    def process(self, dt):
        all_sprites = {}
        for e, (sprite, position) in self.world.get_components(Sprite, Position):
            sprite.apply_changes()
            layer = all_sprites.setdefault((sprite.draw_layer, position.level), set())
            layer.add(sprite._arcade_sprite)

        layers = []
        for e, (draw_layer, sprite_list, in_level) in self.world.get_components(
            DrawLayer, SpriteList, InLevel
        ):
            layers.append((draw_layer.priority, in_level.level_ent))

        for layer, level_ent in all_sprites:
            if (layer, level_ent) not in layers:
                sprite_list = arcade.SpriteList()
                self.world.create_entity(
                    DrawLayer(layer, sprite_list),
                    SpriteList(sprite_list),
                    InLevel(level_ent),
                )

        # TODO: clean up unused draw layers

        for _, (draw_layer, sprite_list, in_level) in self.world.get_components(
            DrawLayer, SpriteList, InLevel
        ):
            sprites_in_layer = all_sprites.get(
                (draw_layer.priority, in_level.level_ent), []
            )
            for arcade_sprite in list(sprite_list._arcade_sprite_list):
                if arcade_sprite not in sprites_in_layer:
                    sprite_list._arcade_sprite_list.remove(arcade_sprite)

            for arcade_sprite in sprites_in_layer:
                if arcade_sprite not in sprite_list._arcade_sprite_list.sprite_list:
                    sprite_list._arcade_sprite_list.append(arcade_sprite)


class PlayerFacingProcessor(esper.Processor):
    def process(self, dt):
        for _, (mp, sprite, facing) in self.world.get_components(
            MultiplayerIdentifier, Sprite, Facing
        ):
            sprite._arcade_sprite.texture = player_texture_for(
                mp.colour, facing.direction
            )


def init(world):
    world.add_processor(PlayerFacingProcessor())
    world.add_processor(SpriteProcessor())
    world.add_processor(SpriteListProcessor())
