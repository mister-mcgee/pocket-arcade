import board
import digitalio

class Input:
  BUTTON_1 = 0
  BUTTON_2 = 1
  BUTTON_3 = 2
  BUTTON_4 = 3

  BUTTON_L = 0
  BUTTON_R = 1
  BUTTON_A = 2
  BUTTON_B = 3

  def __init__(self, stage,
    configure_pin_button_1 = board.A1,
    configure_pin_button_2 = board.A2,
    configure_pin_button_3 = board.A3,
    configure_pin_button_4 = board.A4,
  ):
    self.stage = stage

    self.button_1 = digitalio.DigitalInOut(configure_pin_button_1)
    self.button_2 = digitalio.DigitalInOut(configure_pin_button_2)
    self.button_3 = digitalio.DigitalInOut(configure_pin_button_3)
    self.button_4 = digitalio.DigitalInOut(configure_pin_button_4)
    self.button_1.switch_to_input(digitalio.Pull.DOWN)
    self.button_2.switch_to_input(digitalio.Pull.DOWN)
    self.button_3.switch_to_input(digitalio.Pull.DOWN)
    self.button_4.switch_to_input(digitalio.Pull.DOWN)

    self.state = [
      self.button_1.value,
      self.button_2.value,
      self.button_3.value,
      self.button_4.value
    ]

  def is_button_up  (self, button):
    return not self.state[button]

  def is_button_down(self, button):
    return     self.state[button]
  
  def poll(self):
    self.poll_button(Input.BUTTON_1, self.button_1.value)
    self.poll_button(Input.BUTTON_2, self.button_2.value)
    self.poll_button(Input.BUTTON_3, self.button_3.value)
    self.poll_button(Input.BUTTON_4, self.button_4.value)

  def poll_button(self, button, value):
    if self.state[button] != value:
      self.state[button]  =  value
      if self.stage.scene != None:
        if value: self.stage.scene.on_button_down(button, self)
        else    : self.stage.scene.on_button_up  (button, self)