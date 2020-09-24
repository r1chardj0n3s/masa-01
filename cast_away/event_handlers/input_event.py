from cast_away.components.input_source import ITEM_1, ITEM_2, ITEM_3
from cast_away.components.inventory import Inventory, InventoryItem
from cast_away.event_dispatch import Message, INPUT, USE_ITEM, USE_SLOT, dispatch, register_listener


ITEM_INVENTORY_INDEX = [ITEM_1, ITEM_2, ITEM_3]


def handle_input(world, message):
    input_event = message.payload['input']

    # CONVERT ITEM_N input into activate item N
    if input_event.input in ITEM_INVENTORY_INDEX:
        dispatch(
            world,
            Message(
                USE_SLOT,
                dict(
                    player_ent=message.payload["player_ent"],
                    index=ITEM_INVENTORY_INDEX.index(input_event.input),
                ),
            ),
        )


def use_slot(world, message):
    inventory = world.component_for_entity(message.payload['player_ent'], Inventory)
    try:
        item_ent = inventory.item_ents[message.payload['index']]
    except IndexError:
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
