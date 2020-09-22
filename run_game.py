import arcade
import sys

from cast_away.window import Game
from cast_away.entities import init

init()

if len(sys.argv) > 1:
    game = Game(sys.argv[1])
else:
    game = Game()
arcade.run()
