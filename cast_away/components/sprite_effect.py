import math


class SpriteEffects:
    def __init__(self, *effects):
        self.effects = list(effects)

    def add(self, effect):
        self.effects.append(effect)


class SpinEffect:
    def __init__(self, play_time, speed):
        self.play_time = play_time
        self.speed = speed
        self.applied = 0

    def clear(self, sprite):
        sprite.angle -= self.applied

    def run(self, dt, sprite):
        add = int(dt * self.speed)
        sprite.angle += add
        self.applied += add

class TwistEffect:
    def __init__(self, play_time, size):
        self.play_time = play_time
        self._play_time = self.play_time
        self.size = size * 360
        self.applied = 0

    def clear(self, sprite):
        sprite.angle -= self.applied

    def run(self, dt, sprite):
        u = min(1, (self._play_time - self.play_time) / self._play_time)
        u = int(math.sin(2 * u * math.pi) * self.size)
        self.applied += u
        sprite.angle += u


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


class FadeEffect:
    def __init__(self, play_time, to_alpha=0):
        self._play_time = play_time
        self.play_time = play_time
        self.to_alpha = to_alpha
        self.initial_alpha = None

    def clear(self, sprite):
        pass

    def run(self, dt, sprite):
        if self.initial_alpha is None:
            self.initial_alpha = sprite.alpha

        u = min(1, (self._play_time - self.play_time) / self._play_time)
        sprite.alpha = u * self.to_alpha + (1 - u) * self.initial_alpha


class ScaleUpDownEffect:
    def __init__(self, play_time, to_scale=2):
        self._play_time = play_time
        self.play_time = play_time
        self.to_scale = to_scale
        self.initial_scale = None

    def clear(self, sprite):
        pass

    def run(self, dt, sprite):
        if self.initial_scale is None:
            self.initial_scale = sprite.scale

        u = min(1, (self._play_time - self.play_time) / self._play_time)
        u = math.sin(u * math.pi)
        # print(u, math.sin(u * math.pi))
        sprite.scale = u * self.to_scale + (1 - u) * self.initial_scale


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