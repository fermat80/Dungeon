from location import Location
from items.master.box import Box
from items.master.keys import BoxKey
from items.master.letter import Letter
from items.master.games import HangmanGame
from items.master.troll import Troll
from items.master.troll import Sword

class Foyer(Location):

  def __init__(self):
    self.id = 'master_foyer'
    self.name = "Foyer of Dungeon Master's House"
    self.description = "You are in the foyer of the dungeon master's house!  On a table, you see a letter that you can 'read'.  There is an open doorway leading to the north, and a dark passage leads west. "
    self.contents = [Letter(), BoxKey(), Sword()]

  def do(self, player, command):

    if (command == 'n' or command == 'north'):
      return self.move_player(player, 'master_gameroom')

    if (command == 'w' or command == 'west'):
      return self.move_player(player, 'master_trollroom')

    return False


class GameRoom(Location):

  def __init__(self):
    self.id = 'master_gameroom'
    self.name = "Dungeon Master's Game Room"
    self.description = 'This is the famed game room of the dungeon master!  There is an open doorway leading south.'
    self.contents = [HangmanGame(), Box()]

  def do(self, player, command):

    if (command == 's' or command == 'south'):
      return self.move_player(player, 'master_foyer')

    return False;

class TrollRoom(Location):

  def __init__(self):
    self.id = 'master_trollroom'
    self.name = "Troll Room"
    self.description = 'This is a small room with a passage to the east and a forbidding hole leading west.  Bloodstains and deep scratches (perhaps made by an axe) mar the walls.'
    self.contents = [Troll()]

  def do(self, player, command):

    if (command == 'e' or command == 'east'):
      return self.move_player(player, 'master_foyer')

    if (command == 'w' or command == 'west'):

      for x in self.contents:
        if x.id == 'master_troll' and x.attack_count < 4:
          print('The troll blocks your passage with an evil grin.')
          return True
        return self.move_player(player, 'master_trollhole')

    return False;

class TrollHole(Location):

  def __init__(self):
    self.id = 'master_trollhole'
    self.name = "Troll Hole"
    self.description = 'A nasty little hole with bones scattered about. A hole in the wall leads east.'
    self.contents = []

  def do(self, player, command):

    if (command == 'e' or command == 'east'):
      return self.move_player(player, 'master_trollroom')

    return False;

