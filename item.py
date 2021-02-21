import settings

class Item():

  can_be_taken = True

  def is_named(self, name):
    return self.id.lower() == name.lower()

  def is_my_command(self, user_command, item_command):
    return user_command.startswith(item_command+' ') and self.is_named(user_command[len(item_command)+1:])

  def get_description(self):
    return self.description

  def can_be_taken_by(self, player):
    return self.can_be_taken

  def move_player(self, player, location_name):
    player.location = settings.dungeon.locations[location_name]
    player.location.display()

  def do(self, player, command):
    return False

  def unlock(self, command, parms):
    return None
