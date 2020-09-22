
class UniqueItem:
    def __init__(self, name, position, level_name, size, carried_by=None):
        self.name = name
        self.position = position
        self.level_name = level_name
        self.size = size
        self.carried_by = carried_by