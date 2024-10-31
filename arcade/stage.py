import gc
import time

import board
import busio
import pwmio
import digitalio
import ulab.numpy as np

from adafruit_rgb_display import st7735

from arcade.scene  import UpdateContext, RenderContext
from arcade.input  import Input
from arcade.canvas import Canvas


class Stage:
  def __init__(self,
    dbg   = False,
    fps   =  20,
    x     =   2,
    y     =   3,
    w     = 128,
    h     = 128,
    cs    = board.D10 ,
    rs    = board.D11 ,
    dc    = board.D12 ,    
    sck   = board.SCK ,
    miso  = board.MISO,
    mosi  = board.MOSI,
    lite  = board.D13 ,
    btn1  = board.A1,
    btn2  = board.A2,
    btn3  = board.A3,
    btn4  = board.A4,
    brite = .5
  ):
    self.input = Input(self, btn1, btn2, btn3, btn4)
    # configuration
    self.cfg_dbg      = dbg
    self.cfg_fps      = fps
    self.cfg_x        = x
    self.cfg_y        = y
    self.cfg_w        = w
    self.cfg_h        = h
    self.cfg_pin_cs   = cs
    self.cfg_pin_rs   = rs
    self.cfg_pin_dc   = dc
    self.cfg_pin_sck  = sck
    self.cfg_pin_miso = miso
    self.cfg_pin_mosi = mosi
    self.cfg_pin_lite = lite

    # metrics
    self.m_fps = 0

    self.m_frame_ms   = 0
    self.m_update_ms  = 0
    self.m_render_ms  = 0
    self.m_system_ms  = 0

    self.m_fps_accumulator = 0

    self.m_frame_ms_accumulator  = 0
    self.m_update_ms_accumulator = 0
    self.m_render_ms_accumulator = 0
    self.m_system_ms_accumulator = 0

    self.m_mem_used = gc.mem_alloc()
    self.m_mem_free = gc.mem_free ()

    # timing
    self.t_t               = 0
    self.t_dt              = 0
    self.t_fixed_dt        = 1   /  self.cfg_fps
    self.t_nanos_per_frame = 1e9 // self.cfg_fps
    self.t_nanos_per_reset = 1e9

    self.t_now   = 0
    self.t_epoch = 0
    self.t_frame = 0
    self.t_reset = 0

    self.t_timing_0 = 0
    self.t_timing_1 = 0
    self.t_timing_2 = 0
    self.t_timing_3 = 0

    self.is_running = False

    self.screen = st7735.ST7735R(
      busio.SPI(
        clock=self.cfg_pin_sck , 
        MOSI =self.cfg_pin_mosi,
        MISO =self.cfg_pin_miso
      ), 
      width    = self.cfg_w, 
      height   = self.cfg_h, 
      rotation = 0,
      x_offset = self.cfg_x,
      y_offset = self.cfg_y,
      cs       = digitalio.DigitalInOut(self.cfg_pin_cs),
      dc       = digitalio.DigitalInOut(self.cfg_pin_dc),
      rst      = digitalio.DigitalInOut(self.cfg_pin_rs),
    )

    self.canvas = Canvas(
      w = self.cfg_w + 1, 
      h = self.cfg_h
    )

    self.lite = pwmio.PWMOut(self.cfg_pin_lite, frequency=1000, duty_cycle=0)
    self.set_brightness(brite)

    self.ucontext = UpdateContext(self)
    self.rcontext = RenderContext(self)
    self.scene    = None

  def set_brightness(self, b):
    self.lite.duty_cycle = int(b * 65535)

  def get_brightness(self   ):
    return  self.lite.duty_cycle / 65535

  def use(self, scene):
    if self.scene:
      self.scene.on_detach(self)
    self.scene = scene
    if self.scene:
      self.scene.on_attach(self)
    self.run()

  def update(self, t, dt, fixed_dt):
    self.input.poll()
    if self.scene:
      self.ucontext.       t =        t
      self.ucontext.      dt =       dt
      self.ucontext.fixed_dt = fixed_dt
      self.scene.on_update(self.ucontext)

  def render(self, t, dt, fixed_dt):
    if self.scene:
      self.rcontext.       t =        t
      self.rcontext.      dt =       dt
      self.rcontext.fixed_dt = fixed_dt
      self.scene.on_render(self.rcontext)

  def blit(self):
    self.screen._block(0, 0, 
      self.cfg_w,
      self.cfg_h,
      self.canvas.buffer
    )

  def run(self):
    if self.is_running: return

    self.is_running = True
    self.t_epoch = time.monotonic_ns()
    self.t_frame = time.monotonic_ns()
    self.t_reset = time.monotonic_ns()

    while True:
      self.t_now = time.monotonic_ns()

      if self.t_now - self.t_frame > self.t_nanos_per_frame:

        self.t_t  = (self.t_now - self.t_epoch) / 1e9
        self.t_dt = (self.t_now - self.t_frame) / 1e9
        
        self.t_timing_0 = time.monotonic_ns()
        self.update(self.t_t, self.t_dt, self.t_fixed_dt)
        self.t_timing_1 = time.monotonic_ns()
        self.render(self.t_t, self.t_dt, self.t_fixed_dt)
        self.t_timing_2 = time.monotonic_ns()
        self.blit()
        self.t_timing_3 = time.monotonic_ns()

        self.m_fps_accumulator       += 1
        self.m_frame_ms_accumulator  += (self.t_timing_3 - self.t_timing_0) // 1e6
        self.m_update_ms_accumulator += (self.t_timing_1 - self.t_timing_0) // 1e6
        self.m_render_ms_accumulator += (self.t_timing_2 - self.t_timing_1) // 1e6
        self.m_system_ms_accumulator += (self.t_timing_3 - self.t_timing_2) // 1e6

        self.t_frame = self.t_now

      if self.t_now - self.t_reset > self.t_nanos_per_reset:
        self.m_fps = self.m_fps_accumulator

        self.m_frame_ms  = self.m_frame_ms_accumulator  / self.m_fps_accumulator
        self.m_update_ms = self.m_update_ms_accumulator / self.m_fps_accumulator
        self.m_render_ms = self.m_render_ms_accumulator / self.m_fps_accumulator
        self.m_system_ms = self.m_system_ms_accumulator / self.m_fps_accumulator

        self.m_fps_accumulator       = 0
        self.m_frame_ms_accumulator  = 0
        self.m_update_ms_accumulator = 0
        self.m_render_ms_accumulator = 0
        self.m_system_ms_accumulator = 0

        self.t_reset = self.t_now

        if self.cfg_dbg:
          self.m_mem_used = gc.mem_alloc()
          self.m_mem_free = gc.mem_free ()

          print("*** DEBUG ***")
          print(f"FRAME : {self.m_fps} hz @ {self.m_frame_ms:.2f} of {1e3 / self.cfg_fps:.2f} ms")
          print(f"UPDATE: {self.m_update_ms:>13.2f} ms")
          print(f"RENDER: {self.m_render_ms:>13.2f} ms")
          print(f"SYSTEM: {self.m_system_ms:>13.2f} ms")
          print(f"MEMORY: {self.m_mem_used // 1000} of {(self.m_mem_used + self.m_mem_free) // 1000} kb {100 * self.m_mem_used // (self.m_mem_used + self.m_mem_free)}%")





