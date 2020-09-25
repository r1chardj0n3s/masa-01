DEFAULT_LAYER=1000
CHARACTER_LAYER=2000
SPRITES_LAYER_Z = 50
PARTICLE_LAYER = 100

class DrawLayer:
    def __init__(self, priority, drawable):
        self.priority = priority
        self.drawable = drawable

    def draw(self):
        self.drawable.draw()

    def __repr__(self):
        return f'<DrawLayer priority={self.priority}>'
