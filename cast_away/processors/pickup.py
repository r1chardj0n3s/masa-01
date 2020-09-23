import esper

from cast_away.components.spawner import PickupSpawner
from cast_away.components.position import Position
from cast_away.components.player import Player

from cast_away.entities.inventory_item import create_inventory_item

from cast_away.event_dispatch import COLLISION, register_listener

def collision(world, message):
    pickup_ent, inventory_ent = message.payload
    spawner = world.component_for_entity(pickup_ent, PickupSpawner)
    item = create_inventory_item(world, inventory_ent, spawner.hud_image, spawner.inventory_item_component_classes)
    print(f"deleting {pickup_ent} FIXME! pickup processor(message handler)")
    world.delete_entity(pickup_ent)

def init(world):
    register_listener(COLLISION, collision)
