from arcade.image import Image
from arcade.scene import Scene
from arcade.stage import Stage


# from arcade.games.chess import Chess
# from arcade.games.debug import Debug
from arcade.games.snake import Snake

stage = Stage(dbg=True)

stage.screen.set_brightness(1)
stage.play(Snake())
stage.loop()
