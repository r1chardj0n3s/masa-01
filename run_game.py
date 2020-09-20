import arcade
import sys

window = arcade.Window(1024, 768, "Junk Yard Wars")

sprites = arcade.SpriteList()

sprite = arcade.Sprite(':resources:images/alien/alienBlue_front.png', center_x=100, center_y=100)
sprites.append(sprite)

my_map = arcade.tilemap.read_tmx("data/first-map.tmx")

background_list = arcade.tilemap.process_layer(my_map, 'Tile Layer 1', 1)

arcade.start_render()
background_list.draw()
sprites.draw()


arcade.run()
