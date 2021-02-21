from item import Item

class Cat(Item):

  def __init__(self):
    self.id = 'kevin_cat'
    self.name = 'Cat'
    self.description = 'A fluffy orange tabby cat :)'

  def do(self, player, command):
    if command == 'pet cat':      
      print('The pet purrs loudly')
      return True
    return False
    
  def is_named(self, name):
    return name == 'Cat' or name == 'Jiggles'
