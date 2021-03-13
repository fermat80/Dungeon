from location import Location
from items.wen.book import Book
from items.wen.flashlight import Flashlight

class Library(Location):

  def __init__(self):
    self.id = 'wen_Library'
    self.name = "Dungeon Library"
    self.description = "You are in the library of the dungeon!  On one of the bookshelves, you'll find a book of spells.  There are spells you can learn to do magics to find ways to get yourself out of the Dungeon. You need the flashlight to to find the book of spells."    
    self.contents = [Book(), Flashlight()]
    #self.contents = [Book()]
    

  def do(self, player, command):
    if (command == 'bookshelf'):
      self.move_player(player, 'wen_bookshelf')
      return True;    

    if (command == 'flashlight'):
      self.move_player(player, 'wen_flashlight')
      return True;    

    return False;

class BookShelf(Location):

  def __init__(self):
    self.id = 'wen_bookshelf'
    self.name = "Bookshelf"
    self.description = 'This is the bookshelf!'
    self.contents = []
    
  def do(self, player, command):
    if (command == 'library'):
      self.move_player(player, 'wen_Library')
      return True; 

    if (command == 'flashlight'):
      self.move_player(player, 'wen_flashlight')
      return True;  

    return False;

class Flash_light(Location):

  def __init__(self):
    self.id = 'wen_flashlight'
    self.name = "Dungeon Flashlight"
    self.description = 'This is the flashlight!'
    self.contents = []
    
  def do(self, player, command):
    if (command == 'library'):
      self.move_player(player, 'wen_Library')
      return True;

    if (command == 'bookshelf'):
      self.move_player(player, 'wen_bookshelf')
      return True;  

    return False;
