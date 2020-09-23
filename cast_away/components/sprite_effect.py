import arcade
import math


class SpriteEffects:
    def __init__(self, *effects):
        self.effects = list(effects)


class SpinEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.initial_angle = None
    
    def clear(self, sprite):
        sprite._arcade_sprite.angle = self.initial_angle

    def run(self, dt, sprite):
        a_sprite = sprite._arcade_sprite
        if self.initial_angle is None:
            self.initial_angle = a_sprite.angle
        a_sprite.angle = a_sprite.angle + dt * self.speed


class FlashEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.direction = -1
        self.initial_alpha = None
    
    def clear(self, sprite):
        sprite._arcade_sprite.alpha = self.initial_alpha

    def run(self, dt, sprite):
        a_sprite = sprite._arcade_sprite
        self.last_alpha = a_sprite.alpha
        if self.initial_alpha is None:
            self.initial_alpha = self.last_alpha
        new_alpha = self.last_alpha - self.direction * self.speed * dt
        if new_alpha < 0:
            new_alpha = 0
            self.direction *= -1
        elif new_alpha > 255:
            new_alpha = 255
            self.direction *= -1
        a_sprite.alpha = new_alpha


class ThrowToEffect:
    def __init__(self, play_time, start_pos, end_pos, height):
        self._play_time = play_time
        self.play_time = play_time
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = height

    def clear(self, sprite):
        bx, by = self.end_pos.x, self.end_pos.y
        sprite._arcade_sprite.center_x = bx
        sprite._arcade_sprite.center_y = by
    
    def run(self, dt, sprite):
        ax, ay = self.start_pos.x, self.start_pos.y
        bx, by = self.end_pos.x, self.end_pos.y
        dx = bx - ax
        dy = by - ay

        u = min(1, (self._play_time - self.play_time) / self._play_time)
        uy = self.height * math.sin(u * math.pi) + dy * u
        ux = dx * u

        sprite._arcade_sprite.center_x = ax + ux
        sprite._arcade_sprite.center_y = ay + uy
