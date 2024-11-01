from arcade import Stage
from arcade.games.demo  import Demo
from arcade.games.snake import Snake

stage = Stage(dbg=True)
stage.use(Snake())
stage.run(       )
