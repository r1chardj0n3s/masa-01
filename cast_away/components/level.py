class Level:
    def __init__(self, name):
        self.name = name

class CurrentLevel:
    def __init__(self, name):
        self.name = name
        self.last_level = name
        self.loaded = False
        self.timestamp = None

class LevelExit:
    def __init__(self, next_level):
        self.next_level = next_level

    def __repr__(self):
        return '<LevelExit next_level={self.next_level}>'
