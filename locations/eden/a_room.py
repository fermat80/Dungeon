from location import Location 
from items.eden.pic import Pic
from items.eden.master_keys import TwoSumKey
from items.eden.master_keys import ShuffleKey

class A_room(Location):
  def __init__(self):
    self.id='a_room'
    self.name='a wizard studying room'
    self.description='Room with light and picture on wall. westsouthwest is a duelling area.'
    self.contents=[Pic(), TwoSumKey(), ShuffleKey()]
  def do(self,player,command):
    if command in ["westsouthwest",'wsw']:
      return self.move_player(player,"B_room")

    

