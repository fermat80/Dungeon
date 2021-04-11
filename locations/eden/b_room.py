from location import Location
from items.eden.witch import Witch

class B_room(Location):
  def __init__(self):
    self.id='practice_room'
    self.name="witch house"
    self.description='witch house with bubbling cauldrons.'
    self.contents=[Witch()]

