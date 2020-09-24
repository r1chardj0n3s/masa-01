import esper
from math import sqrt
from cast_away.components.position import Position
from cast_away.components.desired_velocity import DesiredVelocity
from cast_away.components.follow_path import FollowPath


class FollowPathProcessor(esper.Processor):
    def process(self, dt):
        for ent, (position, desired_velocity, path) in self.world.get_components(
            Position, DesiredVelocity, FollowPath
        ):
            # find next point
            target_x, target_y = path.points[path.current_point]
            step_x = target_x - position.x
            step_y = target_y - position.y
            step = max(sqrt(step_x ** 2 + step_y ** 2), 1)

            # if position is "near" next point then calculate new vector and set current point
            if step < 30:
                if path.current_point == len(path.points) - 1:
                    path.current_point = 0
                else:
                    path.current_point += 1

            vel_x = step_x * path.speed / step
            vel_y = step_y * path.speed / step
            desired_velocity.dx, desired_velocity.dy = (vel_x, vel_y)


def init(world):
    world.add_processor(FollowPathProcessor())
