from item import Item

class Coat(Item):

  def __init__(self):
    self.id = 'Kathrine.coat'
    self.name = 'Coat'
    self.description = "A fluffy orange coat made out of a fluffy orange tabby. "
  

  def do(self, player, command):
    if command== 'coat':
      print("You attempt to wear the coat. It is much to small for you.")
    
        

  def is_named(self, name):
    return name == 'coat'
  
