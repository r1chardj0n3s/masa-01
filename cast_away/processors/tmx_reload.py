import esper

from cast_away.components.level import Level, LevelProgression
from cast_away.entities.level import map_mtime
from cast_away.event_dispatch import dispatch, RELOAD_MAPS, Message


class TMXReloadProcessor(esper.Processor):
    def process(self, dt):
        # Hmm, this is a singleton, we don't need it to be an entity with a component
        lp = self.world.get_component(LevelProgression)
        if not lp:
            return
        _, current_level = lp[0]
        if not current_level.level_ent:
            return

        current_level_name = self.world.component_for_entity(
            current_level.level_ent, Level
        ).name

        for _, level in self.world.get_component(Level):
            if level.tmx_mtime < map_mtime(level.name):
                print(f"RELOAD {level.tmx_mtime} < {map_mtime(level.name)}")
                dispatch(self.world, Message(RELOAD_MAPS, current_level_name))
                return


def init(world):
    world.add_processor(TMXReloadProcessor())
