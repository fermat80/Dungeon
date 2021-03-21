from item import Item

class SpiderBox(Item):

  def __init__(self):
    self.id = 'spider_box'
    self.name = 'Spider Box'
    self.description = 'A shining box'

    self.can_be_taken = False

  def do(self, player, command):
    if command == 'unlock box':
      #if GiantSpider.name == 'Gone Spider':
      #  print('The box clicks open!')
      #else:
      #  print('You cannot open the box, the spider is blocking it')
      return True
    return False
    
  def is_named(self, name):
    return name == 'box'
