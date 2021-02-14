import locations.master.load as master
import locations.kevin.load as kevin
from locations.tower import TowerTop
from items.portal import Portal

from player import Player;

class Dungeon:

  def __init__(self):

    self.locations = {}
    #self.players = {}
    #self.player_locations = {}

    self.locations['tower_top'] = TowerTop()

    self.load_wizard_location(master)
    self.load_wizard_location(kevin)

  def load_wizard_location(self, module):
    wizard_name = module.__name__[len('locations.'):module.__name__.find('.load')]
    locs = self.load_locations(module.locations())
    if locs:
      self.locations['tower_top'].contents.append(Portal(wizard_name,locs[0].id))
      locs[0].contents.append(Portal('wizard','tower_top'))

  def load_locations(self, locations):
    for location in locations:
      self.locations[location.id] = location
    return locations
  
  def run(self):
    print('Welcome to the dungeon!') 
    Player('Player', self.locations['tower_top']).play()