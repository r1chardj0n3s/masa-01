import esper

from cast_away.components.spawner import PickupSpawner
from cast_away.components.position import Position

from cast_away.entities.inventory_item import create_inventory_item

from cast_away.event_dispatch import COLLISION, register_listener


def collision(world, message):
    pickup_ent, inventory_ent = message.payload
    for spawner in world.try_component(pickup_ent, PickupSpawner):
        # TODO rename me "transfer_to_inventory"
        item = create_inventory_item(
            world=world,
            owner_ent=inventory_ent,
            hud_image=spawner.hud_image,
            inventory_item_component_classes=spawner.inventory_item_component_classes,
            pickup_ent=pickup_ent,
        )
        if item is not None:
            position = world.component_for_entity(pickup_ent, Position)
            # TODO "spawner" shouldn't ever have no level :(
            position.level = None


def init(world):
    register_listener(COLLISION, collision)
