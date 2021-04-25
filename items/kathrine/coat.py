from item import Item

class Coat(Item):

  def __init__(self):
    self.id = 'Kathrine.coat'
    self.name = 'Coat'
    self.description = "A fluffy orange coat made out of a fluffy orange tabby cat C:< "

    
        

  def is_named(self, name):
    return name == 'coat'
  
