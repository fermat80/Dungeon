from item import Item
import random
from replit import db

class SumDoor(Item):

  def __init__(self):
    self.id = 'master_sumdoor'
    self.name = 'Sum Door to the east'
    self.description = "The Sum challenge door."    

    self.is_locked = True
    self.can_be_taken = False
    self.save_key = ('master', self.id + "_lock")

    if self.save_key in db:
      self.is_locked = db[self.save_key]

  def get_description(self):

    s = self.description

    if self.is_locked:
      s += ' The door is locked. '
      s += ' Given two numbers, return their sum.'
    else:
      s += ' The door is unlocked!'

    return s

  def is_named(self, name):
    return name in ['door', 'sum', 'sum door']

  def do(self, player, command):

    if self.is_my_command(command, 'enter') or command in ['e', 'east']:

      if self.is_locked:
        print('The {} is locked.'.format(self.name))
        return True
      
      print('The door is unlocked, but the area to the east is not finished yet.')
      return True

    if self.is_my_command(command, 'unlock'):
      if self.try_unlock(player, command):
        db[self.save_key] = self.is_locked
        return True

  def get_cypher(self):
    return (15,20)

  def check_secret(self, cypher, secret):
    return secret == 35

class TwoSumDoor(Item):

  challenge = """
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
  """

  def __init__(self):
    self.id = 'master_twosumdoor'
    self.name = 'Two-Sum Door to the north'
    self.description = "The Two-Sum challenge door."
    self.is_locked = True
    self.can_be_taken = False
    self.save_key = ('master', self.id + "_lock")

    if self.save_key in db:
      self.is_locked = db[self.save_key]

  def get_description(self):

    print('I am in: ' + self.parent.name)

    s = self.description

    if self.is_locked:
      s += ' The door is locked. '
      s += self.challenge
    else:
      s += ' The door is unlocked!'

    return s

  def is_named(self, name):
    return name in ['door', 'two-sum', 'two-sum door', 'twosum', 'twosum door']

  def do(self, player, command):

    if self.is_my_command(command, 'enter') or command in ['n', 'north']:

      if self.is_locked:
        print('The {} is locked.'.format(self.name))
        return True
      
      self.move_player(player, 'master_twosumcloset')
      return True

    #if command == 'unlock door':
    if self.is_my_command(command, 'unlock'):
      if self.try_unlock(player, command):
        db[self.save_key] = self.is_locked
        return True

  def get_cypher(self):

    lst = [random.randint(0,1000) for _ in range(10)]

    i = j = random.randrange(len(lst))
    while j == i:
      j = random.randrange(len(lst)) 

    return (lst, lst[i] + lst[j])

  def check_secret(self, cypher, secret):

    if not secret:
      return False

    nums, target = cypher

    i, j = secret
    return nums[i] + nums[j] == target

    #return self.solve(cypher) == sorted(secret)

  def solve(self, cypher):

    nums, target = cypher

    x = {nums[i]: i for i in range(len(nums))}

    for i in range(len(nums)):
      y = target - nums[i]

      if y in x and i != x[y]:
        return [i, x[y]]

class ShuffleDoor(Item):

  challenge = """
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

   Input: nums = [2,5,1,3,4,7], n = 3
   Output: [2,3,5,4,1,7]
"""

  def __init__(self):
    self.id = 'master_shuffledoor'
    self.name = 'Shuffle Door to the west'
    self.description = "The Shuffle challenge door."

    self.is_locked = True
    self.can_be_taken = False
    self.save_key = ('master', self.id + "_lock")
    
    if self.save_key in db:
      self.is_locked = db[self.save_key]

    self.locks = {
      ((2,5,1,3,4,7), 3): [2,3,5,4,1,7],
      ((1,2,3,4,4,3,2,1), 4): [1,4,2,3,3,2,4,1]
    }

  def get_description(self):

    s = self.description

    if self.is_locked:
      s += ' The door is locked. '
      s += self.challenge
    else:
      s += ' The door is unlocked!'

    return s

  def is_named(self, name):
    return name in ['door', 'shuffle', 'shuffle door']

  def do(self, player, command):

    if self.is_my_command(command, 'enter') or command in ['w', 'west']:

      if self.is_locked:
        print('The {} is locked.'.format(self.name))
        return True
      
      self.move_player(player, 'master_shufflecloset')
      return True

    if self.is_my_command(command, 'unlock'):
      if self.try_unlock(player, command):
        db[self.save_key] = self.is_locked
        return True

  def get_cyphers(self):
    #return [((2,5,1,3,4,7), 3), ((1,2,3,4,4,3,2,1), 4)]
    return self.locks.keys()

  def check_secret(self, cypher, secret):
    
    #if cypher == ((2,5,1,3,4,7), 3):
    #  return secret == [2,3,5,4,1,7]
    #if cypher == ((2,5,1,3,4,7), 3):
    #  return secret == [2,3,5,4,1,7]

    return secret == self.locks[cypher]

class MediumDoor(Item):

  challenge = """
Challenge coming soon!
"""

  def __init__(self):
    self.id = 'master_mediumdoor'
    self.name = 'Medium Door to the east'
    self.description = "The medium challenge door. A work in progress."

    self.is_locked = True
    self.can_be_taken = False
    self.save_key = ('master', self.id + "_lock")
    
    if self.save_key in db:
      self.is_locked = db[self.save_key]

  def get_description(self):

    s = self.description

    if self.is_locked:
      s += ' The door is locked. '
      s += self.challenge
    else:
      s += ' The door is unlocked!'

    return s

  def is_named(self, name):
    return name in ['door', 'medium', 'medium door']

  def do(self, player, command):

    if self.is_my_command(command, 'enter') or command in ['e', 'east']:

      if self.is_locked:
        print('The {} is locked.'.format(self.name))
        return True
      
      print('The door is unlocked, but the area to the east is not finished yet.')
      return True

    if self.is_my_command(command, 'unlock'):
      if self.try_unlock(player, command):
        db[self.save_key] = self.is_locked
        return True

  def get_cypher(self):
    return None

  def check_secret(self, cypher, secret):
    return False
