from cast_away.event_dispatch import (
    register_listener,
    COLLISION,
)

from cast_away.entities.sound import create_sound
from cast_away.components.sprite_effect import ScaleUpDownEffect, SpriteEffects
from cast_away.components.prop import Prop
from cast_away.components.timeout import Timeout


def collision(world, message):
    goat = message.payload[0]
    for prop in world.try_component(goat, Prop):
        if prop.type == "goat":
            if world.has_component(goat, Timeout):
                return
            effects = world.component_for_entity(goat, SpriteEffects)
            effects.effects.append(ScaleUpDownEffect(0.45))
            world.add_component(goat, Timeout(0.5))
            create_sound(world, "data/sound/344057__reitanna__why2.wav")


def init():
    register_listener(COLLISION, collision)
