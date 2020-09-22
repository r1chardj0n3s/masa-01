import arcade
import esper

from ..components.unique_item import UniqueItem 
from ..components.level import CurrentLevel
from ..components.sprite import Sprite

unique_item_sprites = {
    "saw": Sprite(":resources:images/enemies/saw.png", scale=0.2)
}

class UniqueItemProcessor(esper.Processor):
    def process(self, dt):
        world = self.world
        for _, item in world.get_component(UniqueItem):
            def find_sprite():
                for e, (sprite, i) in world.get_components(Sprite, UniqueItem):
                    if i == item:
                        return e
            sprite = find_sprite()
            if not item.carried:
                for _, cl in self.world.get_component(CurrentLevel):
                    if cl.name == item.level_name and sprite is None:
                            world.create_entity(unique_item_sprites.get(item.name), item.position, item)
                    elif sprite is not None:
                        world.delete_entity(sprite, immediate=True)
            else:
                world.delete_entity(sprite, immediate=True)

def init(world):
    world.add_processor(UniqueItemProcessor())
