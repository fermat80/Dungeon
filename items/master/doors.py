from item import Item
import random

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

  def get_description(self):

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

    if self.is_my_command(command, 'enter') or command == 'n' or command == 'north':

      if self.is_locked:
        print('The {} is locked.'.format(self.name))
        return True
      
      print('The door is unlocked, but the area to the north is not finished yet.')
      return True

    #if command == 'unlock door':
    if self.is_my_command(command, 'unlock'):
      return self.try_unlock(player, command)

  def get_cypher(self):

    lst = [random.randint(0,1000) for _ in range(10)]

    i = j = random.randrange(len(lst))
    while j == i:
      j = random.randrange(len(lst)) 

    return (lst, lst[i] + lst[j])

  def check_secret(self, cypher, secret):

    if not secret:
      return False

    return self.solve(cypher) == sorted(secret)

  def solve(self, cypher):

    nums, target = cypher

    x = {nums[i]: i for i in range(len(nums))}

    for i in range(len(nums)):
      y = target - nums[i]

      if y in x and i != x[y]:
        return [i, x[y]]




