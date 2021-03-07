from location import Location
from items.master.box import Box
from items.master.keys import BoxKey
from items.master.letter import Letter
from items.master.games import HangmanGame
from items.master.doors import TwoSumDoor
from items.master.doors import SumDoor
from items.master.keys import TwoSumKey
from items.master.keys import SumKey
from items.master.creatures import Dragon

class Foyer(Location):

  def __init__(self):
    self.id = 'master_foyer'
    self.name = "Foyer of Dungeon Master's House"
    self.description = "You are in the foyer of the dungeon master's house!  On a table, you see a letter that you can 'read'.  There is an open doorway leading to the north."    
    self.contents = [Letter(), BoxKey()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'master_gameroom')
      return True;     
    return False;

class GameRoom(Location):

  def __init__(self):
    self.id = 'master_gameroom'
    self.name = "Dungeon Master's Game Room"
    self.description = 'This is the famed game room of the dungeon master!  There is an open doorway leading south.  The challenge area is to the east.'
    self.contents = [HangmanGame(), Box()]

  def do(self, player, command):

    if (command == 's' or command == 'south'):
      self.move_player(player, 'master_foyer')
      return True;     

    if (command == 'e' or command == 'east'):
      self.move_player(player, 'master_challengearea')
      return True;     

    return False;

class ChallengeArea(Location):

  def __init__(self):
    self.id = 'master_challengearea'
    self.name = 'Challenge Area'
    self.description = 'This is the entrance to the coding challenge area!  The easy challenges are north, medium challenges east, and hard challenges south (beware, there be dragons).  The game room is to the west.'
    self.contents = []

  def do(self, player, command):

    if (command == 'w' or command == 'west'):
      self.move_player(player, 'master_gameroom')
      return True;     

    if (command == 'n' or command == 'north'):
      self.move_player(player, 'master_easychallengeroom')
      return True;     

    if (command == 'e' or command == 'east'):
      self.move_player(player, 'master_mediumchallengeroom')
      return True;     

    if (command == 's' or command == 'south'):
      self.move_player(player, 'master_hardchallengeroom')
      return True;     

    return False;

class EasyChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_easychallengeroom'
    self.name = 'Easy Challenge Room'
    self.description = 'This is the easy challenge room!  The challenge area is to the south.'
    self.contents = [TwoSumDoor(), SumDoor()]
    #self.contents = [TwoSumDoor()]

  def do(self, player, command):
    if (command == 's' or command == 'south'):
      self.move_player(player, 'master_challengearea')
      return True;     
    return False;

class MediumChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_mediumchallengeroom'
    self.name = 'Medium Challenge Room'
    self.description = 'This is the medium challenge room!  The challenge area is to the west.'
    self.contents = []

  def do(self, player, command):
    if (command == 'w' or command == 'west'):
      self.move_player(player, 'master_challengearea')
      return True;     
    return False;

class HardChallengeRoom(Location):

  def __init__(self):
    self.id = 'master_hardchallengeroom'
    self.name = 'Hard Challenge Room'
    self.description = 'This is the hard challenge room!  The challenge area is to the north.'
    self.contents = [Dragon()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'master_challengearea')
      return True;     
    return False;
