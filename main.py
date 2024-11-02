from arcade.stage import Stage

from arcade.games.snake import Snake
from arcade.games.debug import Debug

stage = Stage(dbg=True)
stage.use(Debug())
stage.run()
