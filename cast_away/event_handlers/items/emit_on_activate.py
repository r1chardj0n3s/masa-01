from cast_away.event_dispatch import USE_ITEM, register_listener
from cast_away.components.position import Position
from cast_away.components.level import InLevel
from cast_away.components.items.uses import EmitOnActivate, THROW_SOUND
from cast_away.components.graphics.emitter import Emitter
from cast_away.components.draw_layer import DrawLayer, PARTICLE_LAYER
from cast_away.entities.sound import create_sound


def use_emitter(world, message):
    inventory_item_ent = message.payload['item_ent']
    player_ent = message.payload['player_ent']

    for emitter_comp in world.try_component(inventory_item_ent, EmitOnActivate):
        position = world.component_for_entity(player_ent, Position)
        emitter = emitter_comp.emitter_factory(position)
        world.create_entity(
            Emitter(emitter), 
            InLevel(position.level), 
            DrawLayer(PARTICLE_LAYER, emitter)
        )
        create_sound(world, THROW_SOUND)
        


def init():
    register_listener(USE_ITEM, use_emitter)
