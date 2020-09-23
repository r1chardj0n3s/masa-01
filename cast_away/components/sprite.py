import arcade


class Sprite:
    def __init__(self, path, scale=1):
        self._arcade_sprite = arcade.Sprite(path, scale=scale)



class SpriteList:
    def __init__(self):
        self._arcade_sprite_list = arcade.SpriteList()

    def draw(self):
        self._arcade_sprite_list.draw()
