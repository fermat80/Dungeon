from item import Item

class FidgetCube(Item):

  def __init__(self):
    self.id = 'kevin_fidgetcube'
    self.name = 'Fidget Cube'
    self.description = 'A fidget cube with the usual fidget stuff.'

  def do(self, player, command):
    return False
    
  def is_named(self, name):
    return name == 'cube' or name == 'fidget cube'
