
ENTITY_DIED = 'ENTITY_DIED'


class Message:
    def __init__(self, type, payload):
        self.type = type
        self.payload = payload


listeners = {}


def dispatch(world, message):
    for listener in listeners.get(message.type, []):
        listener(world, message)


def register_listener(type, listener):
    listeners.setdefault(type, []).append(listener)
