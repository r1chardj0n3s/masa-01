import arcade
import esper

from .position import Position

class Sprite:
    def __init__(self, path, scale=1):
        self._arcade_sprite = arcade.Sprite(path, scale=scale)


class SpriteList:
    def __init__(self):
        self._arcade_sprite_list = arcade.SpriteList()


class SpriteProcessor(esper.Processor):
    def process(self, dt):
        for _, (sprite, position) in self.world.get_components(Sprite, Position):
            sprite._arcade_sprite.center_x = position.x
            sprite._arcade_sprite.center_y = position.y


class SpriteListProcessor(esper.Processor):
    def process(self, dt):
        for _, sprite_list in self.world.get_component(SpriteList):
            for _, sprite in self.world.get_component(Sprite):
                if (
                    sprite._arcade_sprite
                    not in sprite_list._arcade_sprite_list.sprite_list
                ):
                    sprite_list._arcade_sprite_list.append(sprite._arcade_sprite)

def init(world):
    world.add_processor(SpriteProcessor())
    world.add_processor(SpriteListProcessor())
