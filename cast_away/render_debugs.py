import arcade
from cast_away.components.position import Position
from cast_away.components.velocity import Velocity
from cast_away.components.collidable import HitCircle, HitPoly
from cast_away.components.level import InLevel, Level
from cast_away.components.level.arena_boundary import ArenaBoundary



def render_debugs(world):
    for _, (position, hitCircle) in world.get_components(Position, HitCircle):
        if position.level is not None:
            level = world.component_for_entity(position.level, Level)
            if level.active:
                arcade.draw_circle_filled(
                    position.x, position.y, hitCircle.radius, (255, 0, 0, 100)
                )

    for _, (position, hitPoly) in world.get_components(Position, HitPoly):
        level = world.component_for_entity(position.level, Level)
        if level.active:
            arcade.draw_polygon_outline(hitPoly.point_list, (255, 255, 255, 100), 5)

    for level_ent, boundary in world.get_component(ArenaBoundary):
        level = world.component_for_entity(level_ent, Level)
        if level.active:
            arcade.draw_polygon_outline(boundary.poly.point_list, arcade.color.WHITE, 5)
            for i, point in enumerate(boundary.poly.point_list):
                arcade.draw_text(str(i), point[0], point[1], arcade.color.YELLOW)
    
    for _, (pos, vec) in world.get_components(Position, Velocity):
        level = world.component_for_entity(position.level, Level)
        x1 = pos.x
        x2 = pos.x+vec.dx
        y1 = pos.y
        y2 = pos.y+vec.dy
        if level.active:
            arcade.draw_line(x1,y1, x2,y2, arcade.color.YELLOW, 3)
