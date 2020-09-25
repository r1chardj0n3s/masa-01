import arcade
import sys

from cast_away.window import Game
from cast_away.event_handlers import init_event_handlers

init_event_handlers()

if len(sys.argv) > 1:
    game = Game(sys.argv[1])
else:
    game = Game()
arcade.run()
