from arcade.image import Image
from arcade.scene import Scene

from arcade.fonts import WHITE_ON_BLACK

def Loading(scene):
  class Loading(Scene):
    def on_attach(self, c):
      # draw loading screen
      c.stage.screen.fill(0)
      c.stage.screen.image(Image.load("/arcade/icons/load.bmp"), 56, 56)
      c.stage.screen.blit( )

      c.stage.play(scene)

  return Loading