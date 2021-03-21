from item import Item

class Newspaper(Item):

  def __init__(self):
    self.id = 'Kathrine.newspaper'
    self.name = 'Newspaper'
    self.description = "Today's newspaper"

  def do(self, player, command):
    if command == 'read newspaper'or command=='read paper'or command=='read news':

      article = """
COVID-19 vaccines are safe
Millions of people in the United States have received COVID-19 vaccines, and these vaccines have undergone the most intensive safety monitoring in U.S. history. This monitoring includes using both established and new safety monitoring systems to make sure that COVID-19 vaccines are safe. These vaccines cannot give you COVID-19."""
      print(article)
      return True

      return True 

   

  def is_named(self, name):
    return name == 'newspaper'
  

