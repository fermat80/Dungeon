from item import Item
import random

class SumDoor(Item):
  def __init__(self):
    self.id = 'master_sumdoor'
    self.name = 'Sum Door to the north'
    self.description = ''
    self.is_locked = 0
    
  