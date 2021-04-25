from location import Location
from items.kevin.cat import Cat
from items.kevin.fidget import FidgetCube
from items.kevin.sign import Sign
from items.kevin.spider import GiantSpider
from items.kevin.keys import SumKey
from items.kevin.box import SpiderBox

class HobbitHole(Location):

  def __init__(self):

    self.id = 'hobbit_hole'
    self.name = 'Hobbit Hole'
    self.description = 'You are in a hobbit hole. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it is a hobbit-hole, and that means comfort.'
    self.contents = [FidgetCube(),Sign(),SumKey()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'cat_cafe')
      return True;   

    if (command == 's' or command == 'south'):
      self.move_player(player, 'dark_forest')
      return True;  
    return False;

class CatCafe(Location):

  def __init__(self):

    self.id = 'cat_cafe'
    self.name = 'Cat Cafe'
    self.description = 'A cozy coffee shop with plenty of little friends to keep you company!'
    self.contents = [Cat()]
  
  def do(self, player, command):
    if (command == 's' or command == 'south'):
      self.move_player(player, 'hobbit_hole')
      return True;     
    return False;

class DarkForest(Location):

  def __init__(self):

    self.id = 'dark_forest'
    self.name = 'Dark Forest'
    self.description = 'A dark and eerie forest, mysterious sounds surround you. You have heard many tales of people who never return from these woods.'
    self.contents = [GiantSpider(), SpiderBox()]
  
  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'hobbit_hole')
      return True
    return False