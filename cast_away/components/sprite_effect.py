import arcade
import math


class SpriteEffects:
    def __init__(self, *effects):
        self.effects = list(effects)


class SpinEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.first = True
        self.initial_angle = None
    
    def clear(self, sprite):
        sprite.angle = self.initial_angle

    def run(self, dt, sprite):
        if self.first:
            self.first = False
            if sprite.angle is None:
                sprite.angle = 0
            self.initial_angle = sprite.angle
        sprite.angle = sprite.angle + dt * self.speed


class FlashEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.direction = -1
        self.first = True
        self.initial_alpha = None
    
    def clear(self, sprite):
        sprite.alpha = self.initial_alpha

    def run(self, dt, sprite):
        self.last_alpha = sprite.alpha
        if self.first:
            self.initial_alpha = sprite.alpha
            self.first = False
        new_alpha = self.last_alpha - self.direction * self.speed * dt
        if new_alpha < 0:
            new_alpha = 0
            self.direction *= -1
        elif new_alpha > 255:
            new_alpha = 255
            self.direction *= -1
        sprite.alpha = new_alpha


class ThrowToEffect:
    def __init__(self, play_time, start_pos, end_pos, height):
        self._play_time = play_time
        self.play_time = play_time
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = height

    def clear(self, sprite):
        bx, by = self.end_pos.x, self.end_pos.y
        sprite.center_x = bx
        sprite.center_y = by
    
    def run(self, dt, sprite):
        ax, ay = self.start_pos.x, self.start_pos.y
        bx, by = self.end_pos.x, self.end_pos.y
        dx = bx - ax
        dy = by - ay

        u = min(1, (self._play_time - self.play_time) / self._play_time)
        uy = self.height * math.sin(u * math.pi) + dy * u
        ux = dx * u

        sprite.center_x = ax + ux
        sprite.center_y = ay + uy


class AnimatedTextureEffect:
    def __init__(self, frames):
        self.frames = frames
        self.frame_number = 0
        self.timer = 0
        self.play_time = 100

    def run(self, dt, sprite):
        self.timer -= dt
        if self.timer <= 0:
            self.frame_number += 1
            if self.frame_number == len(self.frames):
                self.frame_number = 0
            self.timer, sprite._arcade_sprite.texture = self.frames[self.frame_number]
        self.play_time = 100