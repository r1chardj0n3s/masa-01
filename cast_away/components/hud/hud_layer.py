class HUDLayer:
    def __init__(self, drawable):
        self.drawable = drawable

    def draw(self):
        self.drawable.draw()