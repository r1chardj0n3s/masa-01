class Sequence:
    def __init__(self, target_ent, *comps):
        self.target_ent = target_ent
        self.comps = list(comps)
        self.active_comp = None
