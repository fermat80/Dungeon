from item import Item

class Letter(Item):

  def __init__(self):
    self.id = 'master_letter'
    self.name = 'Small Letter'
    self.description = "A letter containing a brief message written with a flowing scrawl in bright red ink.  You can 'read' it."

  def do(self, player, command):
    if command == 'read letter':
      print('It reads:  Welcome to the dungeon!')
      return True
    return False

  def is_named(self, name):
    return name == 'letter'
  

