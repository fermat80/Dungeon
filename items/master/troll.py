from item import Item
from replit import db

class Troll(Item):

  def __init__(self):
    self.id = 'master_troll'
    self.name = 'A nasty-looking troll, brandishing a bloody axe, blocks the hole.'
    self.description = 'A nasty-looking troll, brandishing a bloody axe, blocks the hole.'
    self.attack_count = 0

    if ('master', 'troll_attack_count') in db:
      self.attack_count = db[('master', 'troll_attack_count')]
      self.name = db[('master', 'troll_name')]
      self.description = db[('master', 'troll_description')]

  def is_named(self, name):
    return name == 'troll'

  def do(self, player, command):

    if self.is_my_command(command, 'attack') or self.is_my_command(command, 'kill'):

      if 'master_sword' in [x.id for x in player.contents]:
        #print('You attack the troll.')

        if self.attack_count == 0:
          print('Clang! Crash! The troll parries.')
          print('The trolls mighty blow drops you to your knees.')
        elif self.attack_count == 1:
          print('You are still recovering from that last blow, so your attack is ineffective.')
          print('The trolls axe barely misses your ear.')
        elif self.attack_count == 2:
          print('The troll is confused and cant fight back.')
          print('The troll slowly regains his feet.')
        elif self.attack_count == 3:
          print('The troll is knocked out!')
          self.name = 'A knocked out troll.'
          self.description = 'A knocked out troll.'
        elif self.attack_count == 4:
          print('The unarmed troll cannot defend himself: He dies.')
          self.name = 'A dead troll.'
          self.description = 'A dead troll.'

        self.attack_count += 1
        
      else:
        print('You are not carrying the sword!')

      db[('master', 'troll_attack_count')] = self.attack_count
      db[('master', 'troll_name')] = self.name
      db[('master', 'troll_description')] = self.description
   
      return True

    return False

class Sword(Item):

  def __init__(self):
    self.id = 'master_sword'
    self.name = 'An elvish sword of great antiquity.'
    self.description = 'An elvish sword of great antiquity.'

  def is_named(self, name):
    return name == 'sword'
  

