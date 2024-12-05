import supervisor
import microcontroller

from arcade.stage import Stage
from arcade.image import Image

stage = Stage(debug=False)

if   microcontroller.nvm[0:3] == b"dev" and     supervisor.runtime.usb_connected:
  stage.screen.fill(0)
  stage.screen.image(Image.load("/arcade/apps/system/dev.bmp"), 32, 48)
  stage.screen.blit( )
elif microcontroller.nvm[0:3] == b"dev" and not supervisor.runtime.usb_connected:
  # mode mismatch, reset
  microcontroller.nvm[0:3] = b"\0\0\0"
  microcontroller.reset()
elif microcontroller.nvm[0:3] != b"dev" and     supervisor.runtime.usb_connected:
  # mode mismatch, reset
  microcontroller.nvm[0:3] = b"dev"
  microcontroller.reset()

from arcade.apps.system.dashboard import Dashboard
stage.play(Dashboard)
stage.loop()