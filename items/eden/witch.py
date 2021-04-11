from item import Item
#from duel import play

class Witch(Item):
  def __init__(self):
    self.id = "Witch"
    self.name = "Wicked Witch of the Westsouthwest"
    self.description = "Witch that burns enemies. Study up your wizard elements!"
    self.can_be_taken = False
  def is_named(self,name):
    return name in ['witch','bad witch','wicked witch of the westsouthwest']
  def do(self,player,command):
    if command=='duel':
      print("Start duel")
