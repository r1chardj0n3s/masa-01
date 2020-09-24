from dataclasses import dataclass

@dataclass
class Button:
    channel: int

@dataclass
class ButtonChannelListener:
    channel: int
    # function receives params: world, entity_holding_component, entity_that_activated_button
    script: object
    level_ent: object