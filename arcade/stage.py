import gc
import time

from arcade.input   import Input
from arcade.screen  import Screen
from arcade.context import Context

class Stage:
  def __init__(self, *, fps=24, debug=False):
    self.debug = debug

    self.input   = Input  (self)
    self.screen  = Screen (self)
    self.context = Context(self)

    # metrics
    self.m_fps       = 0

    self.m_frame_ms  = 0
    self.m_update_ms = 0
    self.m_render_ms = 0
    self.m_screen_ms = 0

    self.m_fps_accumulator    = 0

    self.m_frame_accumulator  = 0
    self.m_update_accumulator = 0
    self.m_screen_accumulator = 0
    self.m_render_accumulator = 0

    # timing
    self.t        = 0
    self.dt       = 0
    self.fixed_dt = 1 / fps

    self.t_ms_per_frame = 1e3 / fps
    self.t_ns_per_frame = 1e9 / fps
    self.t_ns_per_reset = 1e9

    self.t_now   = 0
    self.t_start = 0
    self.t_frame = 0
    self.t_reset = 0

    self.t_between_0 = 0
    self.t_between_1 = 0
    self.t_between_2 = 0
    self.t_between_3 = 0

    # Scene
    self.scene = None

  def used_kb(self):
    return gc.mem_alloc() / 1000
  
  def free_kb(self):
    return gc.mem_free () / 1000
  
  def total_kb(self):
    return (gc.mem_alloc() + gc.mem_free()) / 1000

  def play(self, scene):
    if self.scene:
      self.scene.on_detach(self.context)

    self.scene =    None
    gc.collect()
    self.scene = scene()

    if self.scene:
      self.scene.on_attach(self.context)

  def update(self, c):
    self.input.poll(c)
    if self.scene:
      self.scene.on_update(c)

  def render(self, c):
    if self.scene:
      self.scene.on_render(c)

  def loop(self):
    self.t_start = time.monotonic_ns()
    self.t_frame = time.monotonic_ns()
    self.t_reset = time.monotonic_ns()

    while True:
      self.t_now = time.monotonic_ns()

      if self.t_now - self.t_frame > self.t_ns_per_frame:

        self.t  = (self.t_now - self.t_start) / 1e9
        self.dt = (self.t_now - self.t_frame) / 1e9

        self.context. t       = self. t
        self.context.dt       = self.dt
        self.context.fixed_dt = self.fixed_dt
        
        self.t_between_0 = time.monotonic_ns()
        self.update(self.context)
        self.t_between_1 = time.monotonic_ns()
        self.render(self.context)
        self.t_between_2 = time.monotonic_ns()
        self.screen.blit()
        self.t_between_3 = time.monotonic_ns()

        self.m_fps_accumulator    += 1
        self.m_frame_accumulator  += (self.t_between_3 - self.t_between_0) // 1e6
        self.m_update_accumulator += (self.t_between_1 - self.t_between_0) // 1e6
        self.m_render_accumulator += (self.t_between_2 - self.t_between_1) // 1e6
        self.m_screen_accumulator += (self.t_between_3 - self.t_between_2) // 1e6

        self.t_frame = self.t_now

      if self.t_now - self.t_reset > self.t_ns_per_reset:
        self.m_fps = self.m_fps_accumulator

        self.m_frame_ms  = self.m_frame_accumulator  / self.m_fps_accumulator
        self.m_update_ms = self.m_update_accumulator / self.m_fps_accumulator
        self.m_render_ms = self.m_render_accumulator / self.m_fps_accumulator
        self.m_screen_ms = self.m_screen_accumulator / self.m_fps_accumulator

        self.m_fps_accumulator    = 0
        self.m_frame_accumulator  = 0
        self.m_update_accumulator = 0
        self.m_render_accumulator = 0
        self.m_screen_accumulator = 0

        self.t_reset = self.t_now

        if self.debug:
          print("*** DEBUG ***")
          print(f"FRAME : {self.m_fps} hz @ {self.m_frame_ms:.2f} of {self.t_ms_per_frame:.2f} ms")
          print(f"UPDATE: {self.m_update_ms:>13.2f} ms")
          print(f"RENDER: {self.m_render_ms:>13.2f} ms")
          print(f"SCREEN: {self.m_screen_ms:>13.2f} ms")
          print(f"MEMORY: {self.used_kb():.2f} of {self.total_kb():.2f} kb {100 * self.used_kb() / self.total_kb():.2f}%")
      
      time.sleep(.001)