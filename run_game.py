import arcade
import esper

keyboard = dict()

world = esper.World()

PLAYER_SPEED = 550
# kenney tiles have fake isometric, 2:1 pixel ratio of diagonals
# the following transformation ensures hitting the controller diagonally
# makes the character move on a "kenney-diagonal" line as drawn on the map
DIMETRIC_FACTOR = 5.0 ** 0.5  # sqrt(5) aka diagonal of a triangle with sides 2, 1 
PLAYER_SPEED_X = PLAYER_SPEED / DIMETRIC_FACTOR
PLAYER_SPEED_Y = PLAYER_SPEED / (DIMETRIC_FACTOR * 2)


class Sprite:
    def __init__(self, path, scale=1):
        self._arcade_sprite = arcade.Sprite(path, scale=scale)


class PlayerControlled:
    ...


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'<Position x={self.x} y={self.y}>'


class Velocity:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def __repr__(self):
        return f'<Velocity dx={self.dx} dy={self.dy}>'

    def scale(self, amount):
        self.dx *= amount
        self.dy *= amount


class GunCooldown:
    def __init__(self, timeout):
        self.timeout = timeout


class Facing:
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
    NORTH = "NORTH"

    def __init__(self, direction):
        self.direction = Facing.EAST

    def velocity(self):
        return {
            Facing.EAST: Velocity(1, 0),
            Facing.WEST: Velocity(-1, 0),
            Facing.NORTH: Velocity(0, 1),
            Facing.SOUTH: Velocity(0, -1),
        }[self.direction]


class Scene:
    ...


class SpriteList:
    def __init__(self):
        self._arcade_sprite_list = arcade.SpriteList()


class PlayerVelocityProcessor(esper.Processor):
    def process(self, dt):
        for _, (pc, velocity) in self.world.get_components(PlayerControlled, Velocity):
            dx = 0
            dy = 0
            if keyboard.get(arcade.key.UP):
                dy += PLAYER_SPEED_Y
            if keyboard.get(arcade.key.DOWN):
                dy -= PLAYER_SPEED_Y
            if keyboard.get(arcade.key.RIGHT):
                dx += PLAYER_SPEED_X
            if keyboard.get(arcade.key.LEFT):
                dx -= PLAYER_SPEED_X
            velocity.dx = dx
            velocity.dy = dy


class PlayerFacingProcessor(esper.Processor):
    def process(self, dt):
        for _, (pc, facing) in self.world.get_components(PlayerControlled, Facing):
            if keyboard.get(arcade.key.UP):
                facing.direction = Facing.NORTH
            if keyboard.get(arcade.key.DOWN):
                facing.direction = Facing.SOUTH
            if keyboard.get(arcade.key.RIGHT):
                facing.direction = Facing.EAST
            if keyboard.get(arcade.key.LEFT):
                facing.direction = Facing.WEST


class VelocityPositionProcessor(esper.Processor):
    def process(self, dt):
        for _, (position, velocity) in self.world.get_components(Position, Velocity):
            position.x += velocity.dx * dt
            position.y += velocity.dy * dt


class SpriteProcessor(esper.Processor):
    def process(self, dt):
        for _, (sprite, position) in self.world.get_components(Sprite, Position):
            sprite._arcade_sprite.center_x = position.x
            sprite._arcade_sprite.center_y = position.y


class SpriteListProcessor(esper.Processor):
    def process(self, dt):
        for _, sprite_list in self.world.get_component(SpriteList):
            for _, sprite in self.world.get_component(Sprite):
                if (
                    sprite._arcade_sprite
                    not in sprite_list._arcade_sprite_list.sprite_list
                ):
                    sprite_list._arcade_sprite_list.append(sprite._arcade_sprite)


class ShootingProcessor(esper.Processor):
    def process(self, dt):
        for ent, (pc, position, facing) in self.world.get_components(
            PlayerControlled, Position, Facing
        ):
            if self.world.has_component(ent, GunCooldown):
                continue
            if keyboard.get(arcade.key.SPACE):
                velocity = facing.velocity()
                velocity.scale(100)
                world.create_entity(
                    Sprite(":resources:images/items/star.png", scale=0.5),
                    Position(x=position.x, y=position.y),
                    velocity,
                )
                self.world.add_component(ent, GunCooldown(.5))


class GunCooldownProcessor(esper.Processor):
    def process(self, dt):
        for ent, cooldown in self.world.get_component(GunCooldown):
            cooldown.timeout -= dt
            if cooldown.timeout <= 0:
                self.world.remove_component(ent, GunCooldown)


world.add_processor(PlayerVelocityProcessor())
world.add_processor(PlayerFacingProcessor())
world.add_processor(GunCooldownProcessor())
world.add_processor(ShootingProcessor())
world.add_processor(VelocityPositionProcessor())
world.add_processor(SpriteListProcessor())
world.add_processor(SpriteProcessor())


def load_object_layer(map, layer_name):
    layer = arcade.tilemap.get_tilemap_layer(map, layer_name)
    map_height = map.map_size.height * map.tile_size[1]
    for obj in layer.tiled_objects:
        obj.location = obj.location._replace(y=map_height - obj.location.y)
    return layer


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Junk Yard Wars")

    def load_map(self, level_map):
        self.scene_entity = world.create_entity(Scene(), SpriteList())
        self.my_map = arcade.tilemap.read_tmx("data/{}.tmx".format(level_map))
        triggers = load_object_layer(self.my_map, "triggers")
        for obj in triggers.tiled_objects:
            if obj.name == "PLAYER_SPAWN":
                world.create_entity(
                    PlayerControlled(),
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Facing(Facing.EAST),
                    Sprite(
                        "data/kenney_robot-pack_side/robot_blueDrive1.png", scale=0.5
                    ),
                )
            if obj.name == "ENEMY_SPAWN":
                world.create_entity(
                    Velocity(0, 0),
                    Position(obj.location.x, obj.location.y),
                    Sprite(":resources:images/enemies/bee.png", scale=0.5),
                )

        self.ground_list = arcade.tilemap.process_layer(self.my_map, "ground")
        self.foreground_list = arcade.tilemap.process_layer(self.my_map, "foreground")

    def on_key_press(self, symbol, modifiers):
        keyboard[symbol] = True
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        # if symbol == arcade.key.SPACE:
        #     self.load_map("second-map")

        # if symbol == arcade.key.ENTER:
        #     bullet = arcade.SpriteSolidColor(20, 5, arcade.color.RED)
        #     self.sprites.append(bullet)
        #     player = world.components_for_entity(1)
        #     world.create_entity(Velocity(200,200), Position(player[3][0], player[3][1]), Sprite(bullet))

    def on_key_release(self, symbol, modifiers):
        del keyboard[symbol]

    def on_update(self, dt):
        world.process(dt)

    def on_draw(self):
        arcade.start_render()
        self.ground_list.draw()
        for _, sprite_list in world.get_component(SpriteList):
            sprite_list._arcade_sprite_list.draw()
        self.foreground_list.draw()


game = Game()
game.load_map("first-map")
arcade.run()
