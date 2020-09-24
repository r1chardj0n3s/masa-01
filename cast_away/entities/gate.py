from cast_away.components.gate import Gate
from cast_away.components.sprite import Sprite
from cast_away.components.barrier import Barrier
from cast_away.components.button import ButtonChannelListener
from cast_away.components.position import Position
from cast_away.components.collidable import Collidable, HitCircle, HitPoly
from cast_away.components.velocity import Velocity

SW = "SW"

GATE_SPRITES = {
    "wooden": {
        SW: ("data/wooden_gate_sw.png", "data/wooden_gate_sw.png", 0.5)
    }
}

def toggle_gate(world, gate_entity, button_presser_ent):
    gate = world.component_for_entity(gate_entity, Gate)
    sprite = world.component_for_entity(gate_entity, Sprite)
    if(world.has_component(gate_entity, Barrier)):
        world.remove_component(gate_entity, Barrier)
        print(f"gate opened by {button_presser_ent}!")
    else:
        world.add_component(gate_entity, Barrier())
        print(f"gate closed by {button_presser_ent}!")

def create_gate(world, obj, level_ent):
    open_path, closed_path, scale = GATE_SPRITES[obj.properties.get("sprite")][obj.properties.get("orientation")]
    world.create_entity(
        Position(obj.x, obj.y, level_ent),
        Collidable(match_components=[Velocity]),
        HitPoly(obj.point_list),
        Barrier(),
        ButtonChannelListener(
            channel = obj.properties.get("channel"),
            script = toggle_gate,
            level_ent = level_ent
        ),
        Sprite(closed_path, scale),
        Gate(open_path, closed_path)
    )
