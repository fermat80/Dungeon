from location import Location
from items.wesley.master_keys import TwoSumKey
from items.wesley.master_keys import ShuffleKey

class Volcano(Location):

  def __init__(self):
    self.id = 'Volcano_Biome'
    self.name = "Volcano"
    self.description = "You find yourself in a Volcano. On the ground you see a book covered with ash, you will need a key to open it."
    self.contents = [TwoSumKey(),ShuffleKey()]
