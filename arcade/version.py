class Version:
  def __init__(self, 
    moniker="", 
    major=0, 
    minor=0, 
    patch=0
  ):
    self.moniker = moniker
    self.major   = major
    self.minor   = minor
    self.patch   = patch

  def __str__(self):
    return f"{self.moniker} {self.major}.{self.minor}.{self.patch}"