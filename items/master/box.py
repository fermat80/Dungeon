import random
from item import Item
from .keys import TwoSumKey
from .keys import SumKey

class Box(Item):

  def __init__(self):

    # These are required for all items...
    self.id = 'master_box'
    self.name = 'Box'
    self.description = 'A black box with a button that you can "push".'

    # This is an extra variable that we will use to keep track of our status.
    self.is_lit = False
    self.is_locked = True

    self.contents = [TwoSumKey(), SumKey()]

  # Single words that allow us to look at or take this object...
  def is_named(self, name):
    return name == 'box'
    
  # This is optional!  But allows you to add code when creating the description.
  # You could also simply change self.description.  See below how we do this with
  # self.name.
  def get_description(self):
    s = self.description

    if self.is_lit:
      s += ' The button is lit!'
    else:
      s += ' The button is not lit.'

    if self.is_locked:
      s += ' The box is locked.  The box can be unlocked with a key that takes a list of numbers and returns them in a sorted list.'
    else:
      s += ' The box is unlocked.'

    return s
  
  def do(self, player, command):

    if command == 'push button':      
      if not self.is_lit:
        print('You push the button on the box and the button lights.')
        self.name = 'A box with a lit button.'
        self.is_lit = True
      else:
        print('You push the lit button on the box and the button turns off.')
        self.name = 'A box.'
        self.is_lit = False
      return True

    #if command == 'unlock box':
    if self.is_my_command(command, 'unlock'):
      return self.try_unlock(player, command)

    return False

  def display_contents(self):
    if not self.is_locked:
      super().display_contents()
    return

  def can_be_taken_from(self, player, item):
    return not self.is_locked

  def can_be_put_into_by(self, player):
    return not self.is_locked

  def get_cypher(self):

    cypher = list(range(10))
    random.shuffle(cypher)

    return cypher

  def check_secret(self, cypher, secret):
    return secret == sorted(cypher)
