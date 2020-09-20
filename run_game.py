import arcade
import esper

keyboard = dict()

world = esper.World()

PLAYER_SPEED = 100


class Sprite():
    def __init__(self, sprite):
        self.sprite = sprite

class PlayerControlled():
    ...

class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Velocity():
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

class PlayerControlProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, velocity) in self.world.get_components(PlayerControlled, Velocity):           
            dx = 0
            dy = 0
            if keyboard.get(arcade.key.UP):
                dy += PLAYER_SPEED
            if keyboard.get(arcade.key.DOWN):
                dy -= PLAYER_SPEED
            if keyboard.get(arcade.key.RIGHT):
                dx += PLAYER_SPEED
            if keyboard.get(arcade.key.LEFT):
                dx -= PLAYER_SPEED
            velocity.dx = dx
            velocity.dy = dy

class VelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for ent, (position, velocity) in self.world.get_components(Position, Velocity):           
            position.x += velocity.dx * dt
            position.y += velocity.dy * dt

class SpriteProcessor(esper.Processor):
    def process(self, dt):
        for ent, (sprite, position) in self.world.get_components(Sprite, Position):           
            sprite.sprite.center_x = position.x
            sprite.sprite.center_y = position.y


world.add_processor(PlayerControlProcessor())
world.add_processor(VelocityPositionProcessor())
world.add_processor(SpriteProcessor())


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Junk Yard Wars")

        self.sprites = arcade.SpriteList()

        sprite = arcade.Sprite(':resources:images/alien/alienBlue_front.png', center_x=100, center_y=100)
        world.create_entity(PlayerControlled(), Velocity(0,0), Position(100, 100), Sprite(sprite))

        self.sprites.append(sprite)   # TODO ECS me??

        self.my_map = arcade.tilemap.read_tmx("data/first-map.tmx")

        self.background_list = arcade.tilemap.process_layer(self.my_map, 'Tile Layer 1')

    def on_key_press(self, symbol, modifiers):
        keyboard[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
        del keyboard[symbol]

    def on_update(self, dt):
        world.process(dt)

    def on_draw(self):
        arcade.start_render()
        self.background_list.draw()
        self.sprites.draw()

game = Game()
arcade.run()
