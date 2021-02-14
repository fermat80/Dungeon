import settings
from dungeon import Dungeon

def main():
  print('Starting the dungeon.')
  settings.dungeon = Dungeon()
  settings.dungeon.run()

if __name__ == "__main__":
    main()
