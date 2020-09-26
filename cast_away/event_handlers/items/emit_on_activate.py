from cast_away.event_dispatch import USE_ITEM, register_listener
from cast_away.components.position import Position
from cast_away.components.items.uses import EmitOnActivate, THROW_SOUND
from cast_away.entities.sound import create_sound
from cast_away.entities.emitter import create_particles


def use_emitter(world, message):
    inventory_item_ent = message.payload['item_ent']
    player_ent = message.payload['player_ent']

    for emitter_comp in world.try_component(inventory_item_ent, EmitOnActivate):
        position = world.component_for_entity(player_ent, Position)
        create_particles(world, emitter_comp.emitter_factory, position)
        create_sound(world, THROW_SOUND)
        


def init():
    register_listener(USE_ITEM, use_emitter)
