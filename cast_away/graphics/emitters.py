import arcade
import random
from cast_away.graphics.particles import AccelleratingParticle

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


FIREWORK_PARTICLE = ":resources:images/items/star.png"


def firework(position):
    x = position.x
    y = position.y
    
    return arcade.Emitter(
        center_xy=(x, y),
        change_xy=(0, 5),
        emit_controller=arcade.EmitterIntervalWithTime(emit_interval=0.1, lifetime=3),
        particle_factory=lambda emitter: arcade.FadeParticle(
            filename_or_texture=FIREWORK_PARTICLE,
            change_xy=arcade.rand_in_circle((0.0, 0.0), 1.0),
            lifetime=1.5,
            scale=0.5 * random.random(),
        ),
    )

