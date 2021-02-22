from item import Item

class GiantSpider(Item):

  def __init__(self):
    self.id = 'giant_spider'
    self.name = 'Giant Spider'
    self.description = 'A giant enemy spider, it looks at you menacingly'

  def do(self, player, command):
    return False

  def is_named(self, name):
    return name == 'spider' or name == 'giant spider'
