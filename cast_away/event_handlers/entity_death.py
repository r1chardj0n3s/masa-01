from cast_away.event_dispatch import register_listener, ENTITY_DIED

from cast_away.components.player import Player
from cast_away.components.inventory import InventoryItem
from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.hud.inventory_display import InventoryHudDisplay
from cast_away.entities.inventory_item import drop_inventory_item

def entity_died(world, message):
    entity = message.payload

    for item_ent, item in world.get_component(InventoryItem):
        if item.owner_ent == entity:
            drop_inventory_item(world, item_ent)

    for hud_ent, display in world.get_component(HealthDisplay):
        if display.player_entity == entity:
            world.delete_entity(hud_ent)

    for hud_ent, display in world.get_component(InventoryHudDisplay):
        if display.player_entity == entity:
            world.delete_entity(hud_ent)

    world.delete_entity(entity)


def init():
    register_listener(ENTITY_DIED, entity_died)