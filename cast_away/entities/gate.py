from cast_away.components.gate import Gate
from cast_away.components.sprite import Sprite
from cast_away.components.barrier import Barrier
from cast_away.components.button import ChannelListener
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitPoly
from cast_away.components.velocity import Velocity
from cast_away.event_handlers.gate import toggle_gate
from cast_away.components.draw_layer import GATES_LAYER

SW = "SW"
SE = "SE"

GATE_SPRITES = {
    "wooden": {
        SW: (
            "data/images/gate_wooden_SW_closed.png",
            "data/images/gate_wooden_SW_open.png",
            1,
        ),
        SE: (
            "data/images/gate_wooden_SE_closed.png",
            "data/images/gate_wooden_SE_open.png",
            1,
        ),
    },
    "metal": {
        SW: (
            "data/images/gate_metal_SW_closed.png",
            "data/images/gate_metal_SW_open.png",
            1,
        ),
        SE: (
            "data/images/gate_metal_SE_closed.png",
            "data/images/gate_metal_SE_open.png",
            1,
        ),
    },
}


def create_gate(world, obj, level_ent):
    level_listen = None
    if obj.properties.get("in_level", False):
        level_listen = level_ent
    closed_path, open_path, scale = GATE_SPRITES[obj.properties.get("sprite")][
        obj.properties.get("orientation")
    ]
    world.create_entity(
        Position(obj.x, obj.y, level_ent),
        Collidable(match_components=[Velocity]),
        HitPoly(obj.point_list),
        Barrier(),
        ChannelListener(
            channel=obj.properties.get("channel"),
            script=toggle_gate,
            level_ent=level_listen,
        ),
        Sprite(closed_path, scale, draw_layer=GATES_LAYER),
        Gate(open_path, closed_path),
    )
