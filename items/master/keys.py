from item import Item

class BoxKey(Item):

  def __init__(self):
    self.id = 'master_box_key'
    self.name = "Dungeon Master's Box Key"
    self.description = "A rather plain key that can open the dungeon master's box."

  def is_named(self, name):
    return name in ['key', 'box key'];

  def unlock(self, item, cypher):  
    return sorted(cypher)

class SumKey(Item):

  def __init__(self):
    self.id = 'master_sumkey'
    self.name = "Sum Key"
    self.description = "A rather plain key that can open the sum door."

  def is_named(self, name):
    return name in ['key', 'sum', 'sum key']

  def unlock(self, item, cypher):
    a, b = cypher
    return a + b

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

    # Add code here to find and return a list of indexes [i,j] where nums[i] + nums[j] = target

    return None

class ShuffleKey(Item):

  def __init__(self):
    self.id = 'master_shufflekey'
    self.name = "Shuffle Key"
    self.description = "A rather plain key that can open the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key']

  def unlock(self, item, cypher):

    lst, n = cypher

    # Add code here to return a new list where the elements of lst are shuffled.

    return None

class SampleKey(Item):

  def __init__(self):
    self.id = 'master_samplekey'
    self.name = "Sample Key"
    self.description = "A rather plain key that can open some door."
  
  def is_named(self, name):
    return name in ['key', 'sample', 'sample key']

  def unlock(self, item, cypher):
    nums, n = cypher

    return nums