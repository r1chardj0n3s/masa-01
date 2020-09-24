from dataclasses import dataclass

@dataclass
class Button:
    channel: str
    in_level: bool

@dataclass
class Channel:
    channel: str
    level_ent: object

@dataclass
class ChannelListener:
    channel: str
    # function receives params: world, entity_holding_component, entity_that_activated_button
    script: object
    level_ent: object
