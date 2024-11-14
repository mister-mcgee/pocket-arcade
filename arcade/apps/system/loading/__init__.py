from arcade.scene import Scene

from arcade.fonts import WHITE_ON_BLACK

def Loading(scene):
  class Loading(Scene):
    def on_attach(self, c):
      # draw loading screen
      c.stage.screen.fill(0)
      c.stage.screen.text(WHITE_ON_BLACK, "Loading...", 34, 60)
      c.stage.screen.blit( )

      c.stage.play(scene)

  return Loading