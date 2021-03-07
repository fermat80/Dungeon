from item import Item

class BoxKey(Item):

  def __init__(self):
    self.id = 'master_box_key'
    self.name = "Dungeon Master's Box Key"
    self.description = "A rather plain key that can open the dungeon master's box."

  def is_named(self, name):
    return name == 'key' or name == 'box key';

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):  
    return sorted(cypher) if cypher else None

class SumKey(Item):

  def __init__(self):
    self.id = 'master_sumkey'
    self.name = "Sum Key"
    self.description = "A rather plain key that can open the sum door."

  def is_named(self, name):
    return name in ['key', 'sum', 'sum key']

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):
    a, b = cypher
    return a+b

class TwoSumKey(Item):

  def __init__(self):
    self.id = 'master_twosumkey'
    self.name = "Two-Sum Key"
    self.description = "A rather plain key that can open the two-sum door."

  def is_named(self, name):
    return name in ['key', 'twosum', 'twosum key', 'two-sum', 'two-sum key']

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):

    nums, target = cypher

    x = {nums[i]: i for i in range(len(nums))}

    for i in range(len(nums)):
      y = target - nums[i]

      if y in x and i != x[y]:
        return [i, x[y]]

    return None
