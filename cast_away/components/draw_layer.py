class DrawLayer:
    def __init__(self, priority, drawable):
        self.priority = priority
        self.drawable = drawable

    def draw(self):
        self.drawable.draw()

    def __repr__(self):
        return f'<DrawLayer priority={self.priority}>'
