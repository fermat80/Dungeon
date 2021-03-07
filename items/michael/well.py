from item import Item

class Well(Item):

  def __init__(self):
    self.id = 'michael.well'
    self.name = 'Well'
    self.description = " It is a well with clear water at the bottom. "
    self.key=True

  def get_description(self):

    s = self.description
    
    if self.key:
      s += 'It is a well with clear water at the bottom. In the bucket of the well, there is a key. You can pick up the key.'
    else:
      s = 'It is a well with clear water at the bottom.'

    return s

  def do(self, player, command):
    if command == 'pick up key' or command=='pick up':
      self.Key=True
      return True      
    return False

  def is_named(self, name):
    return name == 'well'