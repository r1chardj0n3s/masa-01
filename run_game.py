import wasabi2d
import sys

scene = wasabi2d.Scene()

scene.layers[0].add_label("Hello World", pos=(100, 100))

@wasabi2d.event
def on_key_down(key):
    if key == wasabi2d.keys.ESCAPE:
        sys.exit()

wasabi2d.run()
