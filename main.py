from arcade.image import Image
from arcade.scene import Scene
from arcade.stage import Stage

# from arcade.games.chess import Chess
# from arcade.games.debug import Debug
# from arcade.games.snake import Snake
from arcade.games.flappy import Flappy

stage = Stage(dbg=True)

stage.screen.set_brightness(.25)
stage.play(Flappy())
stage.loop()
