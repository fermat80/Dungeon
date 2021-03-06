from location import Location
from items.michael.notes import Note1
from items.michael.notes import Note2
from items.michael.well import Well
from items.michael.door import Door
from items.michael.master_keys import TwoSumKey
from items.michael.master_keys import ShuffleKey

class Basement(Location):

  def __init__(self):
    self.id = 'basement'
    self.name = "The Basement"
    self.description = "The walls are crumbly and you hear bats squeaking. There is a note on the floor. There are two doorways. One leads North and one leads South."    
    self.contents = [Note1(), TwoSumKey(), ShuffleKey()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'michael.well')
      return True; 
    if (command == 's' or command == 'south'):
      self.move_player(player, 'hallway')    
    return False;

class Well_Room(Location):

  def __init__(self):
    self.id = 'michael.well'
    self.name = "Well Room"
    self.description = 'The room is empty, except for a well. There is a note on the side of the well.'
    self.contents = [Note2(), Well()]

  def do(self, player, command):
    if (command == 's' or command == 'south'):
      self.move_player(player, 'basement')
      return True;     
    return False;

class Hallway(Location):

  def __init__(self):
    self.id = 'hallway'
    self.name = "Hallway"
    self.description = 'A hallway with a door on the other side. The door seems to need a key. There is a room to the north.'
    self.contents = [Door()]

  def do(self, player, command):
    if (command == 'n' or command == 'north'):
      self.move_player(player, 'basement')
      return True;
    '''
    if (command == 's' or command == 'north') 
      self.move_player(player, room)
    '''    
    return False;