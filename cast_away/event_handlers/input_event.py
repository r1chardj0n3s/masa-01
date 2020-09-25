from cast_away.components.input_source import ITEM_1, ITEM_2, ITEM_3, DROP
from cast_away.components.inventory import Inventory
from cast_away.event_dispatch import Message, DROP_ITEM, INPUT, USE_ITEM, USE_SLOT, dispatch, register_listener
from cast_away.components.player import Player

ITEM_INVENTORY_INDEX = [ITEM_1, ITEM_2, ITEM_3]


def handle_input(world, message):
    input_event = message.payload['input']
    player_ent = message.payload["player_ent"]

    # CONVERT ITEM_N input into activate item N
    if input_event.input in ITEM_INVENTORY_INDEX:
        input_source = world.component_for_entity(player_ent, Player).input_source
        message_type = USE_SLOT
        if input_source.state.get(DROP):
            message_type = DROP_ITEM
        dispatch(
            world,
            Message(
                message_type,
                dict(
                    player_ent=player_ent,
                    index=ITEM_INVENTORY_INDEX.index(input_event.input),
                ),
            ),
        )


def use_slot(world, message):
    inventory = world.component_for_entity(message.payload['player_ent'], Inventory)
    item_ent = inventory.item_ents[message.payload['index']]
    if item_ent is None:
        return
    dispatch(
        world,
        Message(
            USE_ITEM, dict(player_ent=message.payload['player_ent'], item_ent=item_ent)
        ),
    )


def init():
    register_listener(INPUT, handle_input)
    register_listener(USE_SLOT, use_slot)
