from arcade.image import Image
from arcade.scene import Scene

from arcade.fonts import WHITE_ON_BLACK

load_sprite = Image.load("/arcade/apps/system/load.bmp")

def Loading(scene):
  class Loading(Scene):
    def on_attach(self, c):
      # draw loading screen
      c.stage.screen.fill(0)
      c.stage.screen.image(load_sprite, 56, 56)
      c.stage.screen.blit( )

      c.stage.play(scene)

  return Loading