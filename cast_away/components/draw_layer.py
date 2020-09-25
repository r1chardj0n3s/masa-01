DEFAULT_LAYER=49
CHARACTER_LAYER=50
ITEM_LAYER=5000
GATES_LAYER=5000
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
