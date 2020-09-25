from dataclasses import dataclass

BUTTON_SOUND = ":resources:sounds/rockHit2.ogg"

@dataclass
class Button:
    channel: str
    up_image: str
    down_image: str
    in_level: bool = False
    down_state: bool = False

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
