import arcade
from cast_away.components.position import Position
from cast_away.components.collidable import HitCircle, HitPoly
from cast_away.components.level import Level
from cast_away.components.level.arena_boundary import ArenaBoundary


def render_debugs(world):
    for _, (position, hitCircle) in world.get_components(Position, HitCircle):
        if position.level is not None:
            level = world.component_for_entity(position.level, Level)
            if level.loaded:
                arcade.draw_circle_filled(
                    position.x,
                    position.y,
                    hitCircle.radius,
                    (255,0,0,100)
                )
    for _, (position, hitPoly) in world.get_components(Position, HitPoly):
        level = world.component_for_entity(position.level, Level)
        if level.loaded:
            arcade.draw_polygon_outline(
                hitPoly.point_list,
                (255,255,255,100),
                5
            )

    for _, (boundary, level) in world.get_components(ArenaBoundary, Level):
        if level.loaded:
            arcade.draw_polygon_outline(
                boundary.poly.point_list,
                arcade.color.WHITE,
                5
            )
