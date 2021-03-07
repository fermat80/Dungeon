import settings

class Item():

  can_be_taken = True

  def is_named(self, name):
    return self.id.lower() == name.lower()

  def is_my_command(self, user_command, item_command):

    commands = [x.lower() for x in user_command.split()]

    if commands[0] != item_command:
      return False

    if 'with' in commands:
      idx = commands.index('with')
      item_name = ' '.join(commands[1:idx])
      return self.is_named(item_name)

    item_name = ' '.join(commands[1:])
    return self.is_named(item_name)

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

  def try_unlock(self, player, command):

    commands = [x.lower() for x in command.split()]

    if not self.is_locked:
      print(self.name + ' is already unlocked.')
      return True

    item_name = ''
    if 'with' in commands:
      idx = commands.index('with')
      item_name = ' '.join(commands[idx+1:])      

    cypher = self.get_cypher()

    for item in player.contents:

      if item_name != '' and not item.is_named(item_name):
        continue
     
      print(item.name + ' was given: ' + str(cypher))
      try:
        secret = item.unlock(self, cypher)
      except TypeError:        
        secret = None
      print(item.name + ' returned ' + str(secret))
      if self.check_secret(cypher, secret):
        print('You try the ' + item.name)
        print('Click! {} is unlocked.'.format(self.name))
        self.is_locked = False
        return True

      if item_name != '' and item.is_named(item_name):
        break

    if item_name == '':
      print('None of the items you are carrying seem to unlock ' + self.name)
    elif item:
      print(item.name + ' failed to unlock ' + self.name)
    else:
      print('You do not have ' + item_name)

    return True

  def get_cypher(self):
    return None

  def check_secret(self, cypher, secret):
    return False
