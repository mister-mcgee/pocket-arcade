from arcade.stage import Stage

from arcade.apps.system.dashboard import Dashboard
from arcade.apps.games.blackjack import Blackjack
# from arcade.apps.memory import Memory

stage = Stage(debug=False)
stage.play(Dashboard)
stage.loop()