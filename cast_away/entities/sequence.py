from cast_away.components.sequence import Sequence

def create_sequence(world, target, *comps):
    return world.create_entity(
        Sequence(
            target,
            *comps
        )
    )