from arcade.stage import Stage

from arcade.apps.pong import Pong

stage = Stage(debug=True)
stage.play(Pong)
stage.loop()