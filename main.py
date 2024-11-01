from arcade import Stage

from arcade.games.menu import Menu
from arcade.games.demo import Demo

stage = Stage(dbg=True)
stage.use(Demo())
stage.run(      )
