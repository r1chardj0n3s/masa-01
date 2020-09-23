from cast_away.event_dispatch import register_listener, ENTITY_DIED

from cast_away.components.player import Player
from cast_away.components.inventory import InventoryItem
from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.hud.inventory_display import InventoryHudDisplay
from cast_away.entities.inventory_item import drop_inventory_item
from cast_away.entities.player import create_player
from cast_away.components.multiplayer_identifier import MultiplayerIdentifier

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


def player_respawn(world, message):
    dead_entity = message.payload

    for entity, (player, mp) in world.get_components(Player, MultiplayerIdentifier):
        if entity == dead_entity:
            create_player(world, player.input_source, mp)


def init():
    # potential ordering problem here, watch it!
    register_listener(ENTITY_DIED, player_respawn)
    register_listener(ENTITY_DIED, entity_died)
