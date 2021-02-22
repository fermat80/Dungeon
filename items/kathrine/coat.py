from item import Item

class Coat(Item):

  def __init__(self):
    self.id = 'Kathrine.coat'
    self.name = 'Coat'
    self.description = "A fluffy orange coat. "
  wear_coat=False

  def wear(self, player, command, wear_coat):
    if command == 'wear coat':
      print("You are now wearing a coat.")
      wear_coat=True
  def yn(self, player, command, wear_coat):
    if command == 'clothes':
      if wear_coat==True:
        print("You are wearing a coat.")
        return True
      return False

  def is_named(self, name):
    return name == 'wear'
  
