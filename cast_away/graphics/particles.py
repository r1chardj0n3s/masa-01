from arcade.arcade_types import Point, Vector
from typing import Union
from arcade.draw_commands import Texture
from arcade import LifetimeParticle

FilenameOrTexture = Union[str, Texture]

class AccelleratingParticle(LifetimeParticle):
    def __init__(
            self,
            filename_or_texture: FilenameOrTexture,
            lifetime: float,
            change_xy: Vector = (0,0),
            center_xy: Point = (0.0, 0.0),
            angle: float = 0,
            change_angle: float = 0,
            scale: float = 1.0,
            start_alpha: int = 255,
            end_alpha: int = 0,
            mutation_callback=None,
            accelleration: Vector = (0, 0)
    ):
        super().__init__(filename_or_texture, change_xy, lifetime, center_xy, angle, change_angle, scale, start_alpha,
                         mutation_callback)
        self.start_alpha = start_alpha
        self.end_alpha = end_alpha
        self.accelleration = accelleration

    def update(self):
        super().update()
        self.change_x += self.accelleration[0]
        self.change_y += self.accelleration[1]
        