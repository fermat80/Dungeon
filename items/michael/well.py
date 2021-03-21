from item import Item
from .key import Key

class Well(Item):

  def __init__(self):
    self.id = 'michael.well'
    self.name = 'Well'
    self.description = " It is a well with clear water at the bottom. "
    self.can_be_taken = False
    self.key=True
    self.contents = [Key()]

  def get_description(self):

    s = self.description

    if 'michael_key' in [x.id for x in self.contents]:
      pass

    if self.key:
      s += 'You can pick up the key.'
    else:
      s = 'It is a well with clear water at the bottom and a key in the bucket.'

    return s

  def do(self, player, command):
    if command == 'pick up key' or command=='pick up':
      self.Key=True
      return True      
    return False

  def is_named(self, name):
    return name == 'well'

  def can_be_put_into_by(self, player):
    return True
