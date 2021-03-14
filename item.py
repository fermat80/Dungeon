from replit import db
import settings

class Item(object):

  can_be_taken = True

  def __new__(cls, *args, **kwargs):
    obj = super(Item, cls).__new__(cls)
    obj.contents = []
    return obj

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

  def display(self):
    print(self.get_description())
    self.display_contents()
    return True

  def display_contents(self):
    if len(self.contents) > 0:
      print(' '*2 + 'The {} contains:'.format(self.name))
      for subitem in self.contents:
        print(' '*4 + subitem.name)

  # True if this item can be taken the the player...
  def can_be_taken_by(self, player):
    return self.can_be_taken

  # True if this item is allowed to be put inside this item by the player...
  def can_be_put_into(self, player, item):
    return False

  # True if this item is allowed to be taken out of this item by the player...
  def can_be_taken_from(self, player, item):
    if not item in self.contents:
      return False
    return True

  def move_player(self, player, location_name):
    player.location = settings.dungeon.locations[location_name]
    db[('Dungeon', 'PlayerLocation')] = player.location.id
    player.location.display()
    return True

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

    item = None
    for item in player.contents:

      if item_name != '' and not item.is_named(item_name):
        continue

      all_unlock = True
      for cypher in self.get_cyphers():

        print(item.name + ' was given: ' + str(cypher))
        try:
          secret = item.unlock(self, cypher)
        except:
          secret = None
        print(item.name + ' returned ' + str(secret))
        if not self.check_secret(cypher, secret):
          print('Failed!')
          all_unlock = False
          break

      if all_unlock:
        print('You try the ' + item.name)
        print('Click! {} is unlocked.'.format(self.name))
        self.is_locked = False
        return True

      if item_name != '' and item.is_named(item_name):
        break

    if item_name == '':
      print('None of the items you are carrying seem to unlock ' + self.name)
    elif item and item.is_named(item_name):
      print(item.name + ' failed to unlock ' + self.name)
    else:
      print('You do not have ' + item_name)

    return True

  def get_cyphers(self):
    return [self.get_cypher()]

  def get_cypher(self):
    return None

  def check_secret(self, cypher, secret):
    return False
