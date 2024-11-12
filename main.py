from arcade.stage import Stage

from arcade.games.home import Home

stage = Stage(dbg=False)
stage.play(Home)
stage.loop()
