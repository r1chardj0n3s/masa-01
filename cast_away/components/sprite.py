import arcade


class Sprite:
    def __init__(self, path, scale=1):
        self._arcade_sprite = arcade.Sprite(path, scale=scale)



class SpriteList:
    def __init__(self, _arcade_sprite_list):
        self._arcade_sprite_list = _arcade_sprite_list
