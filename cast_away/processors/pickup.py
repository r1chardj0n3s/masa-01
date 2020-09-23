import esper

from cast_away.components.spawner import PickupSpawner
from cast_away.components.position import Position
from cast_away.components.inventory import Inventory
from cast_away.components.player import Player

from cast_away.entities.inventory_item import create_inventory_item

from cast_away.event_dispatch import COLLISION, register_listener


# when picking things up we create a new entity for the owned item with the
# pickup's component and an Inventory tagged with the player that holds it
# class PickupProcessor(esper.Processor):
#     def process(self, dt):
#         for _, (spawner, spos) in self.world.get_components(PickupSpawner, Position):
#             for player_ent, (pc, ppos) in self.world.get_components(Player, Position):
#                 if spos.distance(ppos) < spawner.component.pickup_distance:
#                     for _, (item, _) in self.world.get_components(Inventory, spawner.component):
#                         if item.owner_ent == player_ent:
#                             break
#                     else:
#                         thrower_ent = create_weapon(self.world, spawner.component())
#                         self.world.add_component(thrower_ent, Inventory(player_ent))

def collision(world, message):
    pickup_ent, inventory_ent = message.payload
    spawner = world.component_for_entity(pickup_ent, PickupSpawner)
    item = create_inventory_item(world, inventory_ent, spawner.inventory_item_component_classes)
    print(f"deleting {pickup_ent} FIXME! pickup processor(message handler)")
    world.delete_entity(pickup_ent)

def init(world):
    register_listener(COLLISION, collision)
    # world.add_processor(PickupProcessor())
