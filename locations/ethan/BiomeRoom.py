from location import Location
from items.ethan.book import Book
from items.ethan.jacket import jacket 
from items.ethan.key import Key 
class BiomeRoom(Location):

  def __init__(self):
    self.id = 'Biome_Room'
    self.name = 'A room with many different ecosystems.'
    self.description = 'You have found the biome room, it is a place with many different creatures in different enviornments.'
    self.contents = [Book(), jacket(), Key()]

