from item import Item

class Dragon(Item):  

  def __init__(self):
    self.id = 'master_dragon'
    self.name = 'Sleeping Dragon'
    self.description = 'A large fire-breathing dragon fills most of the room, blocking any access to challenges.  It appears to be sleeping.'
    self.can_be_taken = False

  def is_named(self, name):
    return name == 'dragon'