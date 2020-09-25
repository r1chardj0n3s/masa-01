from cast_away.components.sequence import Sequence
from cast_away.components.graphics.emitter import Emitter
from cast_away.components.level import InLevel
from cast_away.components.draw_layer import DrawLayer, PARTICLE_LAYER
from cast_away.components.timeout import Timeout
from cast_away.components.position import Position
from cast_away.graphics.emitters import bee_poof
import random
WINDOW_WIDTH=1280
WINDOW_HEIGHT=720

def create_sequence(world, target, *comps):
    return world.create_entity(
        Sequence(
            target,
            *comps
        )
    )

def begin_win_sequence(world, level_ent):
    # for player_ent, player_comp in world.get_component(Player):
    create_sequence(world, 
        level_ent,
        _random_smoke,
        Timeout(1),
        begin_win_sequence,
        Timeout(1)
    )

def _random_smoke(world, level_ent):
    
    x = random.randint(0, WINDOW_WIDTH)
    y = random.randint(0, WINDOW_HEIGHT)
    position = Position(x, y, level_ent)
    emitter = bee_poof(position)
    
    world.create_entity(
        Emitter(emitter), 
        InLevel(position.level), 
        DrawLayer(PARTICLE_LAYER, emitter)
    )