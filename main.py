import settings
from dungeon import Dungeon

def main():
  print('Starting the dungeon.')
  settings.dungeon = Dungeon()
  settings.dungeon.run()

if __name__ == "__main__":
    main()
def __init__(self):
    self.id = 'Flame_Sword'
    self.name = 'Flamesword'
    self.description = 'Slash objects with mass amounts of burning damage'
    
    def do(self, player, command):
      return False
    
    def is_named(self, name):
      return name == 'Sword' or name == 'Flamesword'