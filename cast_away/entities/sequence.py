from cast_away.components.sequence import Sequence
from cast_away.components.graphics.emitter import Emitter
from cast_away.components.timeout import Timeout
from cast_away.graphics.emitters import bee_poof

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
    print("poof!")