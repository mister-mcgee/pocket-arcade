class Version:
  def __init__(self,
    moniker: str = "",
    major  : int =  0,
    minor  : int =  0,
    patch  : int =  0
  ):
    self.moniker = moniker
    self.major   = major
    self.minor   = minor
    self.patch   = patch

  def __str__(self):
    return f"{self.moniker} {self.major}.{self.minor}.{self.patch}"