import board
import digitalio

class Input:
  BUTTON_L = 0
  BUTTON_R = 1
  BUTTON_A = 2
  BUTTON_B = 3

  def __init__(self, 
    stage          ,
    btn1 = board.A1,
    btn2 = board.A2,
    btn3 = board.A3,
    btn4 = board.A4,
  ):
    self.stage = stage

    self.cfg_pin_btn1 = btn1
    self.cfg_pin_btn2 = btn2
    self.cfg_pin_btn3 = btn3
    self.cfg_pin_btn4 = btn4

    self.button_1 = digitalio.DigitalInOut(self.cfg_pin_btn1)
    self.button_2 = digitalio.DigitalInOut(self.cfg_pin_btn2)
    self.button_3 = digitalio.DigitalInOut(self.cfg_pin_btn3)
    self.button_4 = digitalio.DigitalInOut(self.cfg_pin_btn4)

    self.button_1.switch_to_input(digitalio.Pull.DOWN)
    self.button_2.switch_to_input(digitalio.Pull.DOWN)
    self.button_3.switch_to_input(digitalio.Pull.DOWN)
    self.button_4.switch_to_input(digitalio.Pull.DOWN)

    self.buttons = [
      self.button_1.value,
      self.button_2.value,
      self.button_3.value,
      self.button_4.value
    ]

  def get_button(self, id):
    return self.buttons[id]

  def is_button_up  (self, id):
    return not self.buttons[id]

  def is_button_down(self, id):
    return     self.buttons[id]
  
  def poll(self):
    self._poll(Input.BUTTON_L, self.button_1.value)
    self._poll(Input.BUTTON_R, self.button_2.value)
    self._poll(Input.BUTTON_A, self.button_3.value)
    self._poll(Input.BUTTON_B, self.button_4.value)

  def _poll(self, id, value):
    if self.buttons[id] != value:
      self.buttons[id]  =  value
      if self.stage.scene != None:
        if value: self.stage.scene.on_button_down(self, id)
        else    : self.stage.scene.on_button_up  (self, id)


