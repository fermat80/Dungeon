from item import Item

class Book(Item):
  
  def __init__(self):

    self.id = 'biome_book'
    self.name = 'A book of biomes???'
    self.description = 'A strange book with a lot of information about this room.'

    self.is_open = False

  def is_named(self, name):
    return name == 'biome_book'



  def get_description(self):
    if self.is_open:
      return self.description + 'The book is open.'
    return self.description + 'The book is closed.'



  def do(self, player, command):
    if command == 'open book':      
      if not self.is_open:
        print('You open the book about biomes and information pours into your head.')
        self.name = 'A open book'
        self.is_open = True
      else:
        print('You close the strange book and the flow of information stops coming.')
        self.name = 'A closed book'
        self.is_open = False
      return True




