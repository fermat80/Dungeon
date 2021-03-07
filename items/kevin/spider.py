from item import Item

class GiantSpider(Item):

  def __init__(self):
    self.id = 'giant_spider'
    self.name = 'Giant Spider'
    self.description = 'A giant enemy spider, it looks at you menacingly. You see a box right behind the spider. Do you wish to attack?'

  def do(self, player, command):
    if command == 'attack spider' or 'attack giant spider' or 'attack giantspider':      
      
      for item in player.contents:
        if item.name == 'cat':
          
      return True
    return False

  def is_named(self, name):
    return name == 'spider' or name == 'giant spider'
