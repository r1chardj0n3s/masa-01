from cast_away.components.gate import Gate
from cast_away.components.sprite import Sprite
from cast_away.components.barrier import Barrier


def toggle_gate(world, gate_entity, button_presser_ent):
    print("toggle!")
    gate = world.component_for_entity(gate_entity, Gate)
    sprite = world.component_for_entity(gate_entity, Sprite)
    if world.has_component(gate_entity, Barrier):
        world.remove_component(gate_entity, Barrier)
        sprite.alpha = 100
        sprite.path = gate.open_texture
        print(f"gate opened by {button_presser_ent}!")
    else:
        world.add_component(gate_entity, Barrier())
        sprite.alpha = 255
        sprite.path = gate.closed_texture
        print(f"gate closed by {button_presser_ent}!")