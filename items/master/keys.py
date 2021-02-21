from item import Item

class BoxKey(Item):

  def __init__(self):
    self.id = 'master_box_key'
    self.name = "Dungeon Master's Box Key"
    self.description = "A rather plain key that can open the dungeon master's box."

  def is_named(self, name):
    return name == 'key' or name == 'box key';

  def do(self, player, command):    
    return False

  def unlock(self, item, parms):    
    return sorted(parms) if parms else None

