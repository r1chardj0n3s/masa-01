import esper
from cast_away.components.button import Button
from cast_away.components.sprite import Sprite

class ButtonProcessor(esper.Processor):
    def process(self, dt):
        for button_ent, (button, sprite) in self.world.get_components(Button, Sprite):
            if button.down_state:
                sprite.path = button.down_image
            else:
                sprite.path = button.up_image


def init(world):
    world.add_processor(ButtonProcessor())
