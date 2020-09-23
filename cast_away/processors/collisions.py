import esper
import euclid
import random

from cast_away.components.collidable import Collidable, HitPoly, HitCircle
from cast_away.components.position import Position
from cast_away.components.level import Level
from cast_away.components.useful_polygon import is_point_in_polygon

from cast_away.event_dispatch import dispatch, Message, COLLISION

class CollisionDetectionError(Exception):
    pass

def can_collide(world, ea, ca, eb, cb):
    for avoid in ca.avoid_components:
        if world.has_component(eb, avoid):
            return False
    for match in ca.match_components:
        if world.has_component(eb, match):
            return True
    return False

def point(pos, xy):
    x, y = xy
    return (x+pos.x, y+pos.y)

def distance(self, axy, bxy):
    ax, ay = axy
    bx, by = bxy
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

def test_circles(world, ea, eb):
    ca = world.component_for_entity(ea, HitCircle)
    pa = world.component_for_entity(ea, Position)
    cb = world.component_for_entity(eb, HitCircle)
    pb = world.component_for_entity(eb, Position)
    
    return pa.distance(pb) < ca.radius + cb.radius

def test_polys(world, ea, eb):
    raise NotImplementedError("processors/collisions.py")

def test_circle_v_poly(world, circleEntity, polyEntity):
    circle = world.component_for_entity(circleEntity, HitCircle)
    pos = world.component_for_entity(circleEntity, Position)
    poly = world.component_for_entity(polyEntity, HitPoly)
    return poly.is_point_inside(pos.x, pos.y)

def test(world, ea, eb):
    def hit_poly(e):
        return world.has_component(e, HitPoly)
    def hit_circle(e):
        return world.has_component(e, HitCircle)

    if hit_poly(ea) and hit_poly(eb):
        return test_polys(world, ea, eb)
    if hit_poly(ea) and hit_circle(eb):
        return test_circle_v_poly(world, eb, ea)
    if hit_circle(ea) and hit_poly(eb):
        return test_circle_v_poly(world, ea, eb)
    if hit_circle(ea) and hit_circle(eb):
        return test_circles(world, eb, ea)
    raise CollisionDetectionError(f"I don't know how to test these two things for collisions {ea}, {eb}")

def does_collide(world, ea, ca, eb, cb):
    if not can_collide(world, ea, ca, eb, cb):
        return False
    return test(world, ea, eb)

class CollisionProcessor(esper.Processor):
    def process(self, dt):
        #collisions will have a complete bidirectional map of entity -> collisions (two entries per collision)
        collisions = {}
        collidables = self.world.get_components(Collidable, Position)
        #detection
        for ea, (ca, position) in collidables:
            if position.level is not None:
                level = self.world.component_for_entity(position.level, Level)
                if level.loaded:
                    for eb, cb in collidables:
                        if ea == eb: continue
                        if does_collide(self.world, ea, ca, eb, cb):
                            # print(f"found collision! {ca} {cb}")
                            collisions.setdefault(ea, []).append(eb)
        #resolution
        for ea, collisions in collisions.items():
            for eb in collisions:
                # print(f"collision! {ea} {eb}")
                dispatch(self.world, Message(COLLISION, (ea, eb)))

def init(world):
    world.add_processor(CollisionProcessor())

