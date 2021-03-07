from location import Location

class TowerTop(Location):

  def __init__(self):

    # All locations need these...
    self.id = 'tower_top'
    self.name = 'The top of the wizards tower.'
    self.description = 'You are at the top of the wizards tower in a large circular room with stone walls.  Evenly spaced along the walls you see glowing swirling mists... Active portals to the worlds of other wizards!  Down leads to the recently relocated challenge area.'
    self.contents = []    

  def do(self, player, command):

    if command == 'd' or command == 'down':
      return self.move_player(player, 'master_challengearea')
