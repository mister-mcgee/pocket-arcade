from arcade.image import Image
from arcade.scene import Scene
from arcade.stage import Stage

# from arcade.games.chess import Chess
# from arcade.games.debug import Debug
from arcade.games.snake import Snake
# from arcade.games.flappy import Flappy
from arcade.games.home import Home

stage = Stage(dbg=False)

stage.screen.set_brightness(.25)
stage.play(Home)
stage.loop()
