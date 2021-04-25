from location import Location 
from items.eden.pic import Pic

class A_room(Location):
  def __init__(self):
    self.id='a_room'
    self.name='a wizard studying room'
    self.description='room with light and picture on wall westsouthwest is a duelling area.'
    self.contents=[Pic()]
  def do(self,player,command):
    if command in ["westsouthwest",'wsw']:
      return self.move_player(player,"B_room")

    

