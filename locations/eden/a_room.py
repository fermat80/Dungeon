from location import Location 
from items.eden.pic import Pic

class A_room(Location):
  def __init__(self):
    self.id='a_room'
    self.name='a wizard studying room'
    self.description='room with light and picture on wall'
    self.contents=[Pic()]

class Practice_Room(Location):
  def __init__(self):
    self.id='practice_room'
    self.name="spell practice room"
    self.description='a wizard practice room'
    self.contents=[]

