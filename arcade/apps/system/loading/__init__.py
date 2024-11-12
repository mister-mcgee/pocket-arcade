from arcade.scene import Scene

from arcade.fonts import WHITE_ON_BLACK

def Loading(scene):
  class Loading(Scene):
    def on_attach(self, stage):
      # draw loading screen
      stage.screen.fill(0)
      stage.screen.text(WHITE_ON_BLACK, "Loading...", 34, 60)
      stage.screen.blit( )

      stage.play(scene)

  return Loading