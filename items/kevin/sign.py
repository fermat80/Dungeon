from item import Item

class Sign(Item):

  def __init__(self):
    self.id = 'hobbit_sign'
    self.name = 'Sign'
    self.description = 'A sign that shows a cat cafe north and the dark forest south'

  def do(self, player, command):
    return False
    
  def is_named(self, name):
    return name == 'sign' or name == 'hobbit sign'
