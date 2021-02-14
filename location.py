import settings

class Location():  

  def display(self):

    print(self.name)
    print(self.get_description())

    if len(self.contents) > 0:
      print('You see here:')
    for item in self.contents:
      print(' '*2 + item.name)

  def get_description(self):
    return self.description

  def move_player(self, player, location_name):
    player.location = settings.dungeon.locations[location_name]
    player.location.display()

  def do(self, player, command):
    return False