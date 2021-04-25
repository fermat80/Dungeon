from location import Location
from items.eden.witch import Witch
from .a_room import A_room

class B_room(Location):
  def __init__(self):
    self.id='B_room'
    self.name="witch house"
    self.description='witch house with bubbling cauldrons.'
    self.contents=[Witch()]
  def do(self,player,command):
    if command in ["ene","eastnortheast"]:
      return self.move_player(player,"A_room")

