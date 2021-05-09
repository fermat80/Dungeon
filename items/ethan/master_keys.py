from item import Item

class TwoSumKey(Item):

  def __init__(self):
    self.id = 'ethan_twosumkey'
    self.name = "Two-Sum Key"
    self.description = "A rather plain key that can open the two-sum door."

  def is_named(self, name):
    return name in ['key', 'twosum', 'twosum key', 'two-sum', 'two-sum key']

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):

    nums, target = cypher

    

    return False

class ShuffleKey(Item):

  def __init__(self):
    self.id = 'ethan_shufflekey'
    self.name = "Shuffle Key"
    self.description = "A rather plain key that can open the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key']

  def unlock(self, item, cypher):
    
    nums = [2,5,1,3,4,7]
    n = 3

    a = [nums[i] for i in range(n)]
    b = [nums[i] for i in range(n, 2*n)]
    
    a = nums[:n]
    b = nums[n:]
    

    out = ((a + b),)
    for j in range(i+1, len(nums)):
      
  

      return out
