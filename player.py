from container import Container;

class Player(Container):

  def __init__(self, name, location):
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

      if command == 'q' or command == 'quit':
        print('Goodbye!')
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

    if command == 'l' or command == 'look':
      self.location.display()
      return True

    if command == 'i' or command == 'inventory':
      print('You are carrying:')
      if len(self.contents) == 0:
        print('  Nothing')
      else:
        for item in self.contents:
          print(' '*2 + item.name)
      return True

    if command.startswith('take '):
      item_name = command[5:]
      for item in self.location.contents:
        if item.is_named(item_name.lower()):
          if item.can_be_taken_by(self):
            self.contents.append(item)
            self.location.contents.remove(item)
            print('You take: ' + item.name)
          else:
            print('You cannot take: ' + item.name)
          return True

      print("You don't see any {} item here.".format(item_name))
      return True

    if command.startswith('drop '):
      item_name = command[5:]
      for item in self.contents:
        if item.is_named(item_name.lower()):
          self.location.contents.append(item)
          self.contents.remove(item)
          print('You drop: ' + item.name)
          return True

      print("You don't have any {}.".format(item_name))
      return True

    if command.startswith('look at ') or command.startswith('examine '):
      item_name = command[8:]

      for item in self.location.contents:
        if item.is_named(item_name.lower()):
          print(item.get_description())
          return True

      for item in self.contents:
        if item.is_named(item_name.lower()):
          print(item.get_description())
          return True

    if command == 'smile':
      print('You smile!')
      return True

    return False

  def get_command(self):
    print(': ', end='');
    return input()