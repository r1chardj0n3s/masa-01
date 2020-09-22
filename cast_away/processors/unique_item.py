import arcade
import esper

from ..components.unique_item import UniqueItem 
from ..components.level import CurrentLevel
from ..components.sprite import Sprite
from ..components.player import Player
from ..components.position import Position

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
            if item.carried_by is None:
                for _, cl in world.get_component(CurrentLevel):
                    if cl.name == item.level_name:
                        if sprite is None:
                            world.create_entity(unique_item_sprites.get(item.name), item.position, item)
                        self.check_pickups(world, item)
                    elif sprite is not None:
                        world.delete_entity(sprite, immediate=True)
            else:
                if sprite is not None:
                    world.delete_entity(sprite, immediate=True)
    
    def check_pickups(self, world, item):
        for _, (player, position) in world.get_components(Player, Position):
            if item.position.distance(position) < item.size:
                item.carried_by = player
                #put in inventory?

def init(world):
    world.add_processor(UniqueItemProcessor())
