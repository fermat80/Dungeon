import locations.eden.load as eden
import locations.ethan.load as ethan
import locations.kathrine.load as kathrine
import locations.kevin.load as kevin
import locations.master.load as master
import locations.michael.load as michael
import locations.selena.load as selena
import locations.wen.load as wen
import locations.wesley.load as wesley
from locations.tower import TowerTop
from items.portal import Portal
from replit import db

from player import Player;

class Dungeon:

  def __init__(self):

    self.locations = {}
    self.items = {}
    #self.players = {}
    #self.player_locations = {}

    self.locations['tower_top'] = TowerTop() 

    modules = [eden, ethan, kathrine, kevin, master, michael, selena, wen, wesley]

    for module in modules:
      self.load_wizard_location(module)

    location_id = 'tower_top'
    if ('Dungeon', 'PlayerLocation') in db:
      location_id = db[('Dungeon', 'PlayerLocation')]

    self.player = Player('Player', self.locations[location_id])

    self.sync_item_locations()

  def load_wizard_location(self, module):
    wizard_name = module.__name__[len('locations.'):module.__name__.find('.load')]
    locs = self.load_locations(module.locations())

    # Add a portal to wizards tower and FIRST location...
    if locs:
      self.locations['tower_top'].contents.append(Portal(wizard_name,locs[0].id))
      locs[0].contents.append(Portal('wizard','tower_top'))

    # Add all items to our item dictionary...
    for location in self.locations.values():
      self.load_items(location)

  def load_items(self, parent):
    for item in parent.contents:
       item.parent = parent
       self.items[item.id] = item
       self.load_items(item)

  def sync_item_locations(self):
    for item in self.items.values():
      save_key = item.location_save_key()
      if save_key in db:
        new_parent_id = db[save_key]
        if new_parent_id != item.parent.id:
          if new_parent_id in self.locations:
            item.move_to(self.locations[new_parent_id])
          elif new_parent_id in self.items:
            item.move_to(self.items[new_parent_id])
          elif new_parent_id == self.player.id:
            item.move_to(self.player)

  def load_locations(self, locations):
    for location in locations:
      self.locations[location.id] = location
    return locations
  
  def run(self):
    print('Welcome to the dungeon!') 
    self.player.play()
