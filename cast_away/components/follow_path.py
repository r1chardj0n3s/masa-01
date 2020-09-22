import arcade

class FollowPath:
    def __init__(self, points):
        self.points = points
        self.current_point = 0
        self.u = 0

    def update(self, dt):        
        self.u += dt
        if self.u > 1:
            self.u -= 1
            self.current_point += 1
            if self.current_point == len(self.points):
                self.current_point = 0
        next_point = self.current_point + 1
        if next_point == len(self.points):
            next_point = 0
        ax, ay = self.points[self.current_point]
        bx, by = self.points[next_point]
        return arcade.lerp(ax, bx, self.u), arcade.lerp(ay, by, self.u)
