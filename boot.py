import storage
import microcontroller

if microcontroller.nvm[0:3] == b"dev":
  from arcade.screen import Screen
  from arcade.image  import Image

  screen = Screen()

  screen.fill(0)
  screen.image(Image.load("/arcade/apps/system/dev.bmp"), 32, 48)
  screen.blit( )

  storage.remount("/", readonly=True )
else:
  storage.remount("/", readonly=False)