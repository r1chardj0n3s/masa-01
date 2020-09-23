import arcade

from cast_away.components.player import Player
from cast_away.components.velocity import Velocity
from cast_away.components.position import Position
from cast_away.components.collidable import HitCircle, Collidable
from cast_away.components.facing import Facing
from cast_away.components.health import Health
from cast_away.components.hud.health_display import HealthDisplay
from cast_away.components.inventory import Inventory, InventoryItem
from cast_away.event_dispatch import ENTITY_DIED, register_listener
from cast_away.entities.hud.health_display import create_health_display
from cast_away.entities.hud.inventory_display import create_player_inventory_hud
from cast_away.components.sprite_effect import SpinEffect, SpriteEffects, ThrowToEffect
from cast_away.components.sequence import Sequence
from cast_away.components.multiplayer_identifier import (
    MultiplayerIdentifier,
    player_sprite_for,
)
from cast_away.components.level import CurrentLevel, Level
from cast_away.components.level.player_spawn import PlayerSpawns


def create_player(world, input_source):
    players = [mp for _, mp in world.get_component(MultiplayerIdentifier)]

    this_player = MultiplayerIdentifier.select(players)
    _, current_level = world.get_component(CurrentLevel)[0]
    level_ent = current_level.level_ent
    player_ent = world.create_entity(
        this_player,
        Velocity(0, 0),
        HitCircle(radius=25),
        Collidable(),
        Facing(Facing.EAST),
        player_sprite_for(this_player.colour, Facing.EAST),
        Health(3),
        Inventory([]),
    )

    spawners = world.component_for_entity(level_ent, PlayerSpawns).spawns
    for spawner in spawners.values():
        if spawner.first:
            break

    world.create_entity(
        Sequence(
            player_ent,
            SpriteEffects(
                ThrowToEffect(
                    1,
                    Position(-100, 0, level_ent),
                    Position(spawner.x, spawner.y, level_ent),
                    400,
                ),
                SpinEffect(1, 720),
            ),
            Player(input_source),
        )
    )

    create_hud(world, player_ent)


def create_hud(world, player_ent):
    create_health_display(world, player_ent)
    create_player_inventory_hud(world, player_ent)
