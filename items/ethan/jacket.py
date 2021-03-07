from item import Item

class jacket(Item):

  def __init__(self):

    self.id = 'winter_jacket'
    self.name = 'jacket'
    self.description = 'A jacket that will keep you warm in the winter.'

    self.put_on = False

  def is_named(self, name):
    return name == 'winter_jacket'

  def get_description(self):
    if self.put_on:
      return self.description + 'You are wearing the jacket.'
    return self.description + 'You are not wearing the jacket.'


  def do(self, player, command):
    if command == 'grab jacket':      
      if not self.put_on:
        print('You put on the jacket and you feel warm.')
        self.name = ' A worn jacket'
        self.put_on = True
      else:
        print('You take off the jacket and the warmth is gone.')
        self.name = 'A unused jacket'
        self.put_on = False
      return True
