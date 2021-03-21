from item import Item

class Key(Item):

  def __init__(self):
    self.id = 'michael.key'
    self.name = 'Key'
    self.description = " A large and rusted key. "

  def get_description(self):
    s = self.description
    return s

  def do(self, player, command):
    if command == 'pick up key' or command=='pick up':
      self.Key=True
      return True      
    return False

  def unlock(self, item, cypher):
    return self.id

  def is_named(self, name):
    return name == 'key'