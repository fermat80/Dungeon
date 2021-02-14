from item import Item

class Portal(Item):

  def __init__(self, name, location_id):

    # All items need these...
    self.id = 'portal_' + name.lower()
    self.name = "A Portal to {}'s domain.'".format(name.capitalize())
    self.description = 'A swirling glowing portal.  You can "enter" it.'

    # Override this so we can't be picked up...
    self.can_be_taken = False

    # Remember the portals name and location it takes you to...
    self.player_name = name.lower()
    self.location_id = location_id

  def do(self, player, command):
    if self.is_my_command(command, 'enter'):
      print('You enter the portal!')
      self.move_player(player, self.location_id)
      return True

  def is_named(self, name):
    return name == 'portal' or name == self.player_name

