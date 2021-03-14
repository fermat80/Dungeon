from location import Location
from items.master.doors import TwoSumDoor
from items.master.doors import SumDoor
from items.master.doors import ShuffleDoor
from items.master.creatures import Dragon
from items.master.badges import EasyChallengeBadge
from items.master.keys import ShuffleKey

class ChallengeArea(Location):

  def __init__(self):
    self.id = 'master_challengearea'
    self.name = 'Challenge Area'
    self.description = 'This is the entrance to the coding challenge area!  The easy challenges are north, medium challenges east, and hard challenges south (beware, there be dragons).  Stone stairs lead up to the top of the wizards tower.'
    self.contents = []

  def do(self, player, command):

    if (command == 'u' or command == 'up'):
      return self.move_player(player, 'tower_top')

    if (command == 'n' or command == 'north'):
      return self.move_player(player, 'master_easychallengeroom')

    if (command == 'e' or command == 'east'):
      if any(['easychallengebadge' in x.id for x in player.contents]):
        return self.move_player(player, 'master_mediumchallengeroom')
      print('A mysterious force prevents you from moving to the medium challenge area.  You must first prove your worth!')
      return True

    if (command == 's' or command == 'south'):
      return self.move_player(player, 'master_hardchallengeroom')

    return False;

class EasyChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_easychallengeroom'
    self.name = 'Easy Challenge Room'
    self.description = 'This is the easy challenge room!  The challenge area is to the south.'
    self.contents = [TwoSumDoor(), SumDoor(), ShuffleDoor(), ShuffleKey()]
    #self.contents = [TwoSumDoor()]

  def do(self, player, command):
    if (command == 's' or command == 'south'):
      return self.move_player(player, 'master_challengearea')
    return False;

class MediumChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_mediumchallengeroom'
    self.name = 'Medium Challenge Room'
    self.description = 'This is the medium challenge room!  The challenge area is to the west.'
    self.contents = []

  def do(self, player, command):
    if (command == 'w' or command == 'west'):
      return self.move_player(player, 'master_challengearea')
    return False;

class HardChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_hardchallengeroom'
    self.name = 'Hard Challenge Room'
    self.description = 'This is the hard challenge room!  The challenge area is to the north.'
    self.contents = [Dragon()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      return self.move_player(player, 'master_challengearea')
    return False;

class TwoSumCloset(Location):

  def __init__(self):
    self.id = 'master_twosumcloset'
    self.name = 'Two-Sum Challenge Closet'
    self.description = 'This is the Two-Sum Challenge Closet!  You could only reach here by successfully unlocking the Two-Sum Door, congratulations!  The easy challenge room is to the south.'
    self.contents = [EasyChallengeBadge(1)]

  def do(self, player, command):
    if (command == 's' or command == 's'):
      return self.move_player(player, 'master_easychallengeroom')
    return False;

class ShuffleCloset(Location):

  def __init__(self):
    self.id = 'master_shufflecloset'
    self.name = 'Shuffle Challenge Closet'
    self.description = 'This is the Shuffle Challenge Closet!  You could only reach here by successfully unlocking the Shuffle Door, congratulations!  The easy challenge room is to the east.'
    self.contents = [EasyChallengeBadge(2)]

  def do(self, player, command):
    if (command == 'e' or command == 'e'):
      return self.move_player(player, 'master_easychallengeroom')
    return False;
