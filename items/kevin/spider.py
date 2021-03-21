from item import Item

class GiantSpider(Item):

  def __init__(self):
    self.id = 'giant_spider'
    self.name = 'Giant Spider'
    self.description = 'A giant enemy spider, it looks at you menacingly. You see a box right behind the spider. Do you wish to attack?'

  def do(self, player, command):

    if command in ['attack spider', 'attack giant spider', 'attack giantspider']:      
      
      for item in player.contents:
        if item.name == 'Cat':
          print('The cat frantically tries to get out of your arms to attack the spider! The spider flees!')
          self.name = 'Gone Spider'
          self.description = 'The spider has been chased deep into the forest'
          return True
      
      print('The spider spins you in a web! You feel yourself being dragged somewhere')
      self.move_player(player, 'hobbit_hole')
      return True
      
    return False

  def is_named(self, name):
    return name == 'spider' or name == 'giant spider'
