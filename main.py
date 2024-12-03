from arcade.stage import Stage

from arcade.apps.system.dashboard import Dashboard

stage = Stage(debug=False)
stage.play(Dashboard)
stage.loop()