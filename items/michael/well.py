from item import Item

class Well(Item):

  Key=False

  def __init__(self):
    self.id = 'Michael.Well'

    self.name = 'Well'

    self.description = " The water in the well is wet and clear. In the bucket of the well, there is a key. You can pick up the key."

  def do(self, player, command):
    if command == 'pick up key' or command=='pick up':
      self.Key=True
      return True      
    return False

  def is_named(self, name):
    return name == 'Well'