from replit import db
from item import Item;

class Player(Item):

  def __init__(self, name, location):
    self.id = 'player'
    self.name = name
    self.description = 'A player named ' + name
    self.location = location
    self.contents = []

  def play(self):

    self.location.display()

    while self.do_command():
      pass

  def do_command(self):

    command_done = False
    while not command_done:

      command = self.get_command()

      if self.do_quit(command) or self.do_reset(command):
        return False

      if not command_done:
        for item in self.contents:
          if item.do(self, command):
            command_done = True
            break

      if not command_done:
        for item in self.location.contents:
          if item.do(self, command):
            command_done = True
            break

      if not command_done and (self.do(command) or self.location.do(self, command)):
        command_done = True

      if not command_done:
        print('I cannot do that.')

    return True

  def do(self, command):

    todo = [
      self.do_look,
      self.do_inventory,
      self.do_take,
      self.do_put,
      self.do_drop,
      self.do_examine,
      self.do_emote
      ]

    for func in todo:
      if func(command):
        return True
    
    return False
  
  def do_quit(self, command):
    
    if command == 'q' or command == 'quit':
      print('Goodbye!')
      return True

  def do_look(self, command):

    if command == 'l' or command == 'look':
      self.location.display()
      return True

  def do_inventory(self, command):

    if command == 'i' or command == 'inventory':
      print('You are carrying:')
      if len(self.contents) == 0:
        print('  Nothing')
      else:
        for item in self.contents:
          print(' '*2 + item.name)
      return True

  def do_take(self, command):

    if command.startswith('take '):

      commands = [x.lower() for x in command.split()]
   
      if 'from' in commands:
        idx = commands.index('from')
        item_name = ' '.join(commands[1:idx])
        from_item_name = ' '.join(commands[idx+1:])      

        for from_item in self.location.contents + self.contents:
          if from_item.is_named(from_item_name):            
            for item in from_item.contents:
              if item.is_named(item_name):
                if from_item.can_be_taken_from(self, item):
                  item.move_to(self)
                  print('You take: ' + item.name)
                else:
                  print('You cannot take: ' + item.name)
                return True
                
            print("You don't see any {} inside {}.".format(item_name, from_item_name))
            return True

      item_name = command[5:]
      for item in self.location.contents:
        if item.is_named(item_name.lower()):
          if item.can_be_taken_by(self):
            item.move_to(self)
            print('You take: ' + item.name)
          else:
            print('You cannot take: ' + item.name)
          return True

      print("You don't see any {} item here.".format(item_name))
      return True

  def do_put(self, command):

    if command.startswith('put '):

      commands = [x.lower() for x in command.split()]

      if 'in' in commands:
        idx = commands.index('in')
      elif 'into' in commands:
        idx = commands.index('into')
      else:
        return False
        
      item_name = ' '.join(commands[1:idx])
      in_item_name = ' '.join(commands[idx+1:])

      for item in self.contents:
        if item.is_named(item_name):
          for in_item in self.contents + self.location.contents:
            if in_item.is_named(in_item_name):
              if in_item.can_be_put_into(self, item):
                item.move_to(in_item)
                print('You put {} in {}'.format(item.name, in_item.name))
              else:
                print('You cannot put {} in {}'.format(item.name, in_item.name))
              return True
          print("You don't see any {} here.".format(in_item_name))
          return True
      print("You don't see any {} here.".format(item_name))
      return True

  def do_drop(self, command):

    if command.startswith('drop '):
      item_name = command[5:]
      for item in self.contents:
        if item.is_named(item_name.lower()):
          item.move_to(self.location)
          print('You drop: ' + item.name)
          return True

      print("You don't have any {}.".format(item_name))
      return True

  def do_examine(self, command):

    if command.startswith('l at ') or command.startswith('look at ') or command.startswith('examine '):
      words = command.split()
      item_name = ' '.join(words[1:]) if words[0] == 'examine' else ' '.join(words[2:])

      for item in self.location.contents + self.contents:
        if item.is_named(item_name.lower()):
          item.display()
          return True

  def do_emote(self, command):

    if command == 'smile':
      print('You smile!')
      return True

  def do_reset(self, command):

    if command == 'reset db':
      db.clear()
      print('The database has been reset.')
      return True
    
  def get_command(self):
    print(': ', end='');
    return input()
