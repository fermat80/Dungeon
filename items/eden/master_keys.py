from item import Item

class TwoSumKey(Item):

  def __init__(self):
    self.id = 'eden_twosumkey'
    self.name = "Two-Sum Key"
    self.description = "A rather plain key that can open the two-sum door."

  def is_named(self, name):
    return name in ['key', 'twosum', 'twosum key', 'two-sum', 'two-sum key']

  def unlock(self, item, cypher):

    nums, target = cypher

    # Add code here to find and return a list of indexes [i,j] where nums[i] + nums[j] = target

    return None

class ShuffleKey(Item):

  def __init__(self):
    self.id = 'eden_shufflekey'
    self.name = "Shuffle Key"
    self.description = "A rather plain key that can open the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key']

  def unlock(self, item, cypher):

    lst, n = cypher

    # Add code here to return a new list where the elements of lst are shuffled.

    return None
