from cast_away.components.player import Player
from cast_away.components.level import LevelProgression
from cast_away.components.health import Health, HealthDown
from cast_away.components.position import Position
from cast_away.components.velocity import Velocity
from cast_away.components.position_effects import PositionEffects, ThrowToEffect
from cast_away.entities.sequence import create_sequence
from cast_away.components.invulnerable import Invulnerable
from cast_away.entities.sequence import begin_win_sequence


def EXIT(world, level_ent, obj, target_ent, trigger_source_ent):
    if world.has_component(target_ent, Player):
        next_level = obj.properties["next_level"]
        for _, (current_level,) in world.get_components(LevelProgression):
            current_level.next_level = next_level


def SPIKE(world, level_ent, obj, target_ent, trigger_source_ent):
    if world.has_component(target_ent, Player):
        health = world.component_for_entity(target_ent, Health)
        health.effects.append(HealthDown(1))

        if not world.has_component(target_ent, Invulnerable):
            # and knockback
            pos = world.component_for_entity(target_ent, Position)
            velocity = world.component_for_entity(target_ent, Velocity)
            p1 = pos.point2()
            p2 = p1 - velocity.vector2().normalized() * 50
            create_sequence(
                world,
                target_ent,
                PositionEffects(
                    [
                        ThrowToEffect(
                            0.5,
                            Position(p1.x, p1.y, pos.level),
                            Position(p2.x, p2.y, pos.level),
                            100,
                        )
                    ]
                ),
            )


def WIN(world, level_ent, obj, target_ent, trigger_source_ent):
    world.delete_entity(trigger_source_ent)
    begin_win_sequence(world, level_ent)
