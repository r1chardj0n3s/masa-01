import arcade
import esper

keyboard = dict()

world = esper.World()

PLAYER_SPEED = 500


class Sprite:
    def __init__(self, sprite):
        self.sprite = sprite


class PlayerControlled:
    ...


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Velocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


class PlayerControlProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, velocity) in self.world.get_components(
            PlayerControlled, Velocity
        ):
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

    def load_map(self, level_map):
        self.sprites = arcade.SpriteList()
        sprite = arcade.Sprite(":resources:images/alien/alienBlue_front.png")
        bee = arcade.Sprite(":resources:images/enemies/bee.png")
        self.sprites.append(sprite)  # TODO ECS me??
        self.sprites.append(bee)  # TODO ECS me??

        self.my_map = arcade.tilemap.read_tmx("data/{}.tmx".format(level_map))
        map_height = self.my_map.map_size.height * self.my_map.tile_size[1]
        for obj in arcade.tilemap.get_tilemap_layer(
            self.my_map, "triggers"
        ).tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                world.create_entity(
                    PlayerControlled(),
                    Velocity(0, 0),
                    Position(obj.location.x, map_height - obj.location.y),
                    Sprite(sprite),
                )
            if obj.name == "ENEMY_SPAWN":
                world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, map_height - obj.location.y),
                    Sprite(bee),
                )

        self.ground_list = arcade.tilemap.process_layer(self.my_map, "ground")
        self.foreground_list = arcade.tilemap.process_layer(self.my_map, "foreground")

    def on_key_press(self, symbol, modifiers):
        keyboard[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.SPACE:
            self.load_map("second-map")

    def on_key_release(self, symbol, modifiers):
        del keyboard[symbol]

    def on_update(self, dt):
        world.process(dt)

    def on_draw(self):
        arcade.start_render()
        self.ground_list.draw()
        self.sprites.draw()
        self.foreground_list.draw()


game = Game()
game.load_map("first-map")
arcade.run()
