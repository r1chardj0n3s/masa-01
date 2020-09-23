class Level:
    def __init__(self, name, tile_map):
        self.name = name
        self.tile_map = tile_map

class CurrentLevel:
    def __init__(self, name):
        self.name = name
        self.last_level = name
        self.loaded = False
        self.timestamp = None
