import esper

FREQUENCY = 5


class DebugProbeProcessor(esper.Processor):
    def __init__(self):
        self.timer = FREQUENCY

    def process(self, dt):
        self.timer -= dt
        if self.timer > 0:
            return
        self.timer = FREQUENCY

        # print("\n\nLEVELS:")
        # for level_ent, level_comp in self.world.get_component(Level):
        #     print(f"level {level_ent}\n\t{self.world.components_for_entity(level_ent)}")


def init(world):
    world.add_processor(DebugProbeProcessor())
