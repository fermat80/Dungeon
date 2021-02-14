from location import Location
from items.master.box import Box
from items.master.letter import Letter
from items.master.games import HangmanGame

class Foyer(Location):

  def __init__(self):
    self.id = 'master_foyer'
    self.name = "Foyer of Dungeon Master's House"
    self.description = "You are in the foyer of the dungeon master's house!  On a table, you see a letter that you can 'read'.  There is an open doorway leading to the north."    
    self.contents = [Letter()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'master_gameroom')
      return True;     
    return False;

class GameRoom(Location):

  def __init__(self):
    self.id = 'master_gameroom'
    self.name = "Dungeon Master's Game Room"
    self.description = 'This is the famed game room of the dungeon master!  There is an open doorway leading south.'
    self.contents = [HangmanGame(), Box()]

  def do(self, player, command):
    if (command == 's' or command == 'south'):
      self.move_player(player, 'master_foyer')
      return True;     
    return False;
