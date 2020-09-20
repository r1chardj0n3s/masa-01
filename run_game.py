import arcade
import sys

keyboard = dict()

class Game(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "Junk Yard Wars")

        self.sprites = arcade.SpriteList()

        self.sprite = arcade.Sprite(':resources:images/alien/alienBlue_front.png', center_x=100, center_y=100, scale=.5)
        self.sprites.append(self.sprite)

        self.my_map = arcade.tilemap.read_tmx("data/first-map.tmx")

        self.background_list = arcade.tilemap.process_layer(self.my_map, 'Tile Layer 1', .5)

    def on_key_press(self, symbol, modifiers):
        keyboard[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
        del keyboard[symbol]

    def on_update(self, dt):
        if keyboard.get(arcade.key.UP):
            self.sprite.center_y += 5
        if keyboard.get(arcade.key.DOWN):
            self.sprite.center_y -= 5
        if keyboard.get(arcade.key.RIGHT):
            self.sprite.center_x += 5
        if keyboard.get(arcade.key.LEFT):
            self.sprite.center_x -= 5

    def on_draw(self):
        arcade.start_render()
        self.background_list.draw()
        self.sprites.draw()

game = Game()
arcade.run()
