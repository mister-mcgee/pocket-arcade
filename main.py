import supervisor
import microcontroller

if   microcontroller.nvm[0:3] == b"dev" and not supervisor.runtime.usb_connected:
  # mode mismatch, reset
  microcontroller.nvm[0:3] = b"\0\0\0"
  microcontroller.reset()
elif microcontroller.nvm[0:3] != b"dev" and     supervisor.runtime.usb_connected:
  # mode mismatch, reset
  microcontroller.nvm[0:3] = b"dev"
  microcontroller.reset()

from arcade.stage import Stage
from arcade.apps.system.dashboard import Dashboard

stage = Stage(debug=False)
stage.play(Dashboard)
stage.loop()