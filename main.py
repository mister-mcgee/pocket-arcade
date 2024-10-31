from arcade import Stage, Scene, Input, Image, BLACK, WHITE
from arcade.games.demo import Demo

stage = Stage(dbg=True)
stage.use(Demo())
stage.run(      )
