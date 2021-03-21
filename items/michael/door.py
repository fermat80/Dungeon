from item import Item

class Door(Item):

  def __init__(self):

    self.id = 'michael.door'
    self.name = 'A Door'
    self.description = 'A door. It seems to require a key that can unlock it.'

    self.is_locked = True

  def is_named(self, name):
    return name == 'door'
    
  def get_description(self):
    s = self.description

    if self.is_locked:
      s += ' The door seems to be locked.'
    else:
      s += ' A dusty wooden door. There is a handle with a keyhole.'

    return s
  
  # Calling try_unlock() will use get_cypher(), unlock(), check_secret().
  def do(self, player, command):
    if self.is_my_command(command, 'unlock'):
      return self.try_unlock(player, command)

  # The key was modified to have its unlock() return its id.
  def check_secret(self, cypher, secret):
    return secret == 'michael.key'
