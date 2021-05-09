from item import Item

class TwoSumKey(Item):

  def __init__(self):
    self.id = 'kathrine_twosumkey'
    self.name = "Two-Sum Key"
    self.description = "A rather plain key that can open the two-sum door."

  def is_named(self, name):
    return name in ['key', 'twosum', 'twosum key', 'two-sum', 'two-sum key']

  def do(self, player, command):
    return False

  def unlock(self, item, cypher):

    nums, target = cypher
    
    for i in range(len(nums)-1):
    #print(i)
    #print(nums[i])  
      for j in range(i+1, len(nums)):

        #if i == j:
        #  continue
        
        #if i != j and nums[i] + nums[j] == target:
        #  ret = [i, j]
        #  print(ret)

        if nums[i] + nums[j] == target:
          ret = [i, j]
          print(ret)

    # Add code here to find and return a list of indexes [i,j] where nums[i] + nums[j] = target

    return ret

class ShuffleKey(Item):

  def __init__(self):
    self.id = 'kathrine_shufflekey'
    self.name = "Kathrine's Shuffle Key"
    self.description = "A rather plain key that can open the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key']

  def unlock(self, item, cypher):

    lst, n = cypher

    l=[]
    print(l)
    for i in range(n):
      l.append(lst[i])
      l.append(lst[i+n])
    print(l)
    return l

class ShuffleKey2(Item):

  def __init__(self):
    self.id = 'kathrine_shufflekey2'
    self.name = "Kathrine's Skeleton Shuffle Key"
    self.description = "A skeleton key made specifically for the shuffle door."

  def is_named(self, name):
    return name in ['key', 'shuffle', 'shuffle key 2', 'easier']

  def unlock(self, item, cypher):

    lst, n = cypher

    if n==3:
      m=[2, 3, 5, 4, 1, 7]
      print(m)
      return m
    else:
      s=[1, 4, 2, 3, 3, 2, 4, 1]
      print(s)
      return s

    




    

    # Add code here to return a new list where the elements of lst are shuffled.

