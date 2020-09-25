from dataclasses import dataclass, field
import math


@dataclass
class PositionEffects:
    effects: object = field(default_factory=lambda: [])


class ThrowToEffect:
    def __init__(self, play_time, start_pos, end_pos, height):
        self._play_time = play_time
        self.play_time = play_time
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = height

    def clear(self, position):
        bx, by = self.end_pos.x, self.end_pos.y
        position.x = bx
        position.y = by

    def run(self, dt, position):
        ax, ay = self.start_pos.x, self.start_pos.y
        bx, by = self.end_pos.x, self.end_pos.y
        dx = bx - ax
        dy = by - ay

        u = min(1, (self._play_time - self.play_time) / self._play_time)
        uy = self.height * math.sin(u * math.pi) + dy * u
        ux = dx * u

        position.x = ax + ux
        position.y = ay + uy
