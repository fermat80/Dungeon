from item import Item

class SpiderBox(Item):

  def __init__(self):
    self.id = 'spider_box'
    self.name = 'Spider Box'
    self.description = 'A shining box'

  def do(self, player, command):
    return False
    
  def is_named(self, name):
    return name == 'box'
