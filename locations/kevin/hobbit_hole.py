from location import Location

class HobbitHole(Location):

  def __init__(self):

    self.id = 'hobbit_hole'
    self.name = 'Hobbit Hole'
    self.description = 'You are in a hobbit hole. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it is a hobbit-hole, and that means comfort.'
    self.contents = []