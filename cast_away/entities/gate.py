from cast_away.components.gate import Gate
from cast_away.components.sprite import Sprite
from cast_away.components.barrier import Barrier
from cast_away.components.button import ButtonChannelListener
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitPoly
from cast_away.components.velocity import Velocity
from cast_away.event_handlers.gate import toggle_gate

SW = "SW"
SE = "SE"

GATE_SPRITES = {
    "wooden": {
        SW: ("data/gate_wooden_closed_sw.png", "data/gate_wooden_open_sw.png", 0.5),
        SE: ("data/gate_wooden_closed_se.png", "data/gate_wooden_open_se.png", 0.5),
    }
}

def create_gate(world, obj, level_ent):
    closed_path, open_path, scale = GATE_SPRITES[obj.properties.get("sprite")][
        obj.properties.get("orientation")
    ]
    world.create_entity(
        Position(obj.x, obj.y, level_ent),
        Collidable(match_components=[Velocity]),
        HitPoly(obj.point_list),
        Barrier(),
        ButtonChannelListener(
            channel=obj.properties.get("channel"),
            script=toggle_gate,
            level_ent=level_ent,
        ),
        Sprite(closed_path, scale),
        Gate(open_path, closed_path),
    )

