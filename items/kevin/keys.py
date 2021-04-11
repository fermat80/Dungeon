from item import Item

class SumKey(Item):

  def __init__(self):
    self.id = 'Kevin_sumkey'
    self.name = "Sum Key"
    self.description = "Key for the sum door"

  def is_named(self, name):
    return name in ['key', 'sum', 'sum key']

  def unlock(self, item, cypher):
    a, b = cypher
    return a + b