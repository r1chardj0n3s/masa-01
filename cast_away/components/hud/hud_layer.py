class HUDLayer:
    def __init__(self, drawable, priority=0):
        self.drawable = drawable
        self.priority = priority

    def draw(self):
        self.drawable.draw()