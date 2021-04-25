from item import Item

class Key(Item):


  def __init__(self):

    self.id = 'Key'
    self.name= 'Key'
    self.description= 'A key that can unlock anything.'


  def is_named(self, name):
    return name == 'Super_key'
  
  def is_named(self, name):
    return name in ['key', 'box key'];

  
  
  def unlock(self, item, cypher):  
    return sorted(cypher)

