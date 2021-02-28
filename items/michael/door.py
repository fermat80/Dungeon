from item import Item

class Door(Item):

  def __init__(self):

    self.id = 'michael.Door'
    self.name = 'A Door'
    self.description = 'A door. It seems to require a key that can unlock it.'

    self.is_locked = True

  def is_named(self, name):
    return name == 'Door'
    
  def get_description(self):
    s = self.description

    if self.is_locked:
      s += ' The door is locked.  The door can be unlocked by a key.'
    else:
      s += ' The door is unlocked.'

    return s
  
  def do(self, player, command):

    if self.is_my_command(command, 'unlock'):

      if not self.is_locked:
        print('The door is already unlocked.')
        return True

      key=True

      for item in player.contents:         
        result = item.unlock(self, key)
        if result==True:
          print('You try the ' + item.name)
          print('You hear a faint click.')
          self.is_locked = False
          return True

      print('None of the items you have seem to unlock the door.')
      return True

    return False

