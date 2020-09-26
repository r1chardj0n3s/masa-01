from dataclasses import dataclass

CHANNEL = "CHANNEL"
ENTITY_DIED = "ENTITY_DIED"
COLLISION = "COLLISION"
INPUT = "INPUT"
USE_SLOT = "USE_SLOT"
USE_ITEM = "USE_ITEM"
DROP_ITEM = "DROP_ITEM"
RELOAD_MAPS = "RELOAD_MAPS"
RESTART_GAME = "RESTART_GAME"


@dataclass
class Message:
    type: str
    payload: object


listeners = {}


def dispatch(world, type, message_payload=None):
    for listener in listeners.get(type, []):
        listener(world, Message(type, message_payload))


def register_listener(type, listener):
    listeners.setdefault(type, []).append(listener)
