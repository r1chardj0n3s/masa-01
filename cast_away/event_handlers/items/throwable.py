from cast_away.event_dispatch import USE_ITEM, register_listener
from cast_away.components.position import Position
from cast_away.components.facing import Facing
from cast_away.components.items.uses import Throwable, THROW_SOUND
from cast_away.entities.item import drop_inventory_item, InventoryItem
from cast_away.entities.sound import create_sound
from cast_away.components.sprite_effect import SpriteEffects, SpinEffect
from cast_away.components.position_effects import PositionEffects, ThrowToEffect


def use_throwable(world, message):
    inventory_item_ent = message.payload['item_ent']
    player_ent = message.payload['player_ent']

    for throwable in world.try_component(inventory_item_ent, Throwable):
        inventory_item = world.component_for_entity(inventory_item_ent, InventoryItem)
        position = world.component_for_entity(player_ent, Position)
        level_ent = position.level
        facing = world.component_for_entity(player_ent, Facing)
        velocity = facing.velocity()
        velocity.magnitude = throwable.throw_distance
        target_x = position.x + velocity.dx
        target_y = position.y + velocity.dy

        level_item_entity = drop_inventory_item(world, inventory_item_ent)
        world.add_component(level_item_entity, SpriteEffects(
            SpinEffect(
                play_time = throwable.throw_speed, 
                speed = throwable.throw_speed * throwable.throw_distance
            )
        ))
        world.add_component(level_item_entity, PositionEffects([
            ThrowToEffect(
                play_time = throwable.throw_speed,
                start_pos = Position(position.x, position.y, level_ent),
                end_pos = Position(target_x, target_y, level_ent),
                height = throwable.throw_distance / 3,
            )]
        ))
        create_sound(world, THROW_SOUND)
        


def init():
    register_listener(USE_ITEM, use_throwable)
