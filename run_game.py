import arcade
import sys

window = arcade.Window(800, 600, "Junk Yard Wars")

sprites = arcade.SpriteList()

sprite = arcade.Sprite(':resources:images/alien/alienBlue_front.png', center_x=100, center_y=100)
sprites.append(sprite)


arcade.start_render()
sprites.draw()


arcade.run()
