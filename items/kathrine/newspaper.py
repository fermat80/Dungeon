from item import Item

class Newspaper(Item):

  def __init__(self):
    self.id = 'Kathrine.newspaper'
    self.name = 'Newspaper'
    self.description = "Today's newspaper. You can 'read' it."

  def do(self, player, command):
    if command == 'read newspaper'or command=='read paper'or command=='read news':

      article = """
Because there are health problems spreading to our realm, the government advises fairies to stay within their mushrooms and refrain from visiting others! When leaving you mushrooms to collect food, please wear a mask! They are being handed out at the city tunnel in your area! Each fairy may take three."""
      print(article)
      return True      
    return False

  def is_named(self, name):
    return name == 'letter'
  

