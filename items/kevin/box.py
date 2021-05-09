from item import Item
from replit import db

class SpiderBox(Item):

  def __init__(self):
    self.id = 'spider_box'
    self.name = 'Spider Box'
    self.description = 'A shining box'
    self.is_locked = True
    self.can_be_taken = False

  def do(self, player, command):
    if command in ['open box', 'open spider box']:
      if db[('kevin', 'spider_status')] == 'gone':
        print('The box clicks open! Theres nothing inside!')
      else:
        print('You cannot open the box, the spider is blocking it')
    return False
    
  def is_named(self, name):
    return name == 'box'
