from arcade.stage import Stage

from arcade.apps.system.dashboard import Dashboard

stage = Stage(debug=False)
stage.screen.set_brightness(.5)
stage.play(Dashboard)
stage.loop()