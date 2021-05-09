from item import Item

class TwoSumKey(Item):

  def __init__(self):
    self.id = 'kevin_twosumkey'
    self.name = "Two-Sum Key"
    self.description = "A rather plain key that can open the two-sum door."

  def is_named(self, name):
    return name in ['key', 'twosum', 'twosum key', 'two-sum', 'two-sum key']

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):

    nums, target = cypher

    # Add code here to find and return a list of indexes [i,j] where nums[i] + nums[j] = target

    for i in range(len(nums)):
      for j in range(len*(nums)):
        if nums[i] + nums[j] == target and i != j:
          ret = [i,j]
    
    return ret

class ShuffleKey(Item):

  def __init__(self):
    self.id = 'kevin_shufflekey'
    self.name = "Shuffle Key"
    self.description = "A rather plain key that can open the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key']

  def unlock(self, item, cypher):

    lst, n = cypher

    # Add code here to return a new list where the elements of lst are shuffled.
    out = []
    a = [list[i] for i in range(n)]
    b = [list[i] for i in range(n, 2*n)]
    for i in range(len(list)):
      out.append(a[i]) 
      out.append(b[i]) 

    return out
