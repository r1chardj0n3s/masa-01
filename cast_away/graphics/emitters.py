import arcade
import random


def bee_poof(position):
    return arcade.Emitter(
    center_xy=(position.x, position.y),
    emit_controller=arcade.EmitBurst(50),
    particle_factory=lambda emitter: arcade.FadeParticle(
        filename_or_texture=random.choice([
            arcade.load_texture("data/kenney_particlePack_1.1/light_01.png"),
            arcade.load_texture("data/kenney_particlePack_1.1/light_02.png"),
            arcade.load_texture("data/kenney_particlePack_1.1/light_03.png"),
        ]),
        change_xy=arcade.rand_in_circle((0.0, 0.0), 1.0),
        lifetime=1.5,
        scale=0.1 * random.random(),
    ),
)
