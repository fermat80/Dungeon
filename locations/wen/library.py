from location import Location
from items.wen.book import Book

class Library(Location):

  def __init__(self):
    self.id = 'wen_Library'
    self.name = "Dungeon Library"
    self.description = "You are in the library of the dungeon!  On one of the bookshelves, you see a book of spells that you can 'read'.  There are spells you can learn to do magics."    
    self.contents = [Book()]

  def do(self, player, command):
    if (command == 'b' or command == 'book'):
      self.move_player(player, 'wen_bookshelf')
      return True;     
    return False;

class BookShelf(Location):

  def __init__(self):
    self.id = 'wen_bookshelf'
    self.name = "Dungeon Library's Bookshelf"
    self.description = 'This is the bookshelf of the dungeon library!'
    self.contents = []
    
  def do(self, player, command):
    if (command == 'l' or command == 'library'):
      self.move_player(player, 'wen_Library')
      return True;     
    return False;
