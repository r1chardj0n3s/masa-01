from cast_away.components.player import Player
from cast_away.components.level import CurrentLevel
from cast_away.components.health import Health, HealthDown

def EXIT(world, level_ent, obj, target):
    if world.has_component(target, Player):
        next_level = obj.properties["next_level"]
        for _, (current_level,) in world.get_components(CurrentLevel):
            current_level.next_level = next_level

def SPIKE(world, level_ent, obj, target):
    if world.has_component(target, Player): 
        health = world.component_for_entity(target, Health)
        health.effects.append(HealthDown(1))
