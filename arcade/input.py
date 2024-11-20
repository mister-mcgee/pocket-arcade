import board
import digitalio

class Input:
  BUTTON_L = 0
  BUTTON_R = 1
  BUTTON_A = 2
  BUTTON_B = 3

  def __init__(self, stage):
    self.stage = stage
    
    self.l = digitalio.DigitalInOut( board.A1 )
    self.r = digitalio.DigitalInOut( board.A2 )
    self.a = digitalio.DigitalInOut( board.A3 )
    self.b = digitalio.DigitalInOut( board.A4 )
    self.l.switch_to_input(digitalio.Pull.DOWN)
    self.r.switch_to_input(digitalio.Pull.DOWN)
    self.a.switch_to_input(digitalio.Pull.DOWN)
    self.b.switch_to_input(digitalio.Pull.DOWN)

    self.state = [
      self.l.value,
      self.r.value,
      self.a.value,
      self.b.value
    ]

  def is_button_up  (self, button):
    return not self.state[button]

  def is_button_down(self, button):
    return     self.state[button]
  
  def poll(self, c):
    self.poll_button(c, Input.BUTTON_L, self.l.value)
    self.poll_button(c, Input.BUTTON_R, self.r.value)
    self.poll_button(c, Input.BUTTON_A, self.a.value)
    self.poll_button(c, Input.BUTTON_B, self.b.value)

  def reset(self):
    self.state = [
      self.l.value,
      self.r.value,
      self.a.value,
      self.b.value
    ]

  def poll_button(self, c, button, value):
    if self.state[button] != value:
      self.state[button]  =  value
      if self.stage.scene != None:
        if value: self.stage.scene.on_button_down(c, button)
        else    : self.stage.scene.on_button_up  (c, button)