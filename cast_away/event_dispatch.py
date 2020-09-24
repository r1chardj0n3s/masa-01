from dataclasses import dataclass

BUTTON = 'BUTTON'
ENTITY_DIED = 'ENTITY_DIED'
COLLISION = 'COLLISION'
INPUT = 'INPUT'
USE_SLOT = 'USE_SLOT'
USE_ITEM = 'USE_ITEM'
DROP_ITEM = 'DROP_ITEM'


@dataclass
class Message:
    type: str
    payload: object


listeners = {}


def dispatch(world, message):
    for listener in listeners.get(message.type, []):
        listener(world, message)


def register_listener(type, listener):
    listeners.setdefault(type, []).append(listener)
