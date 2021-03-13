from item import Item

class Math(Item):

  def __init__(self):
    self.id = 'Kathrine.math'
    self.name = 'Math Problem'
    self.description = "An easy math problem on a piece of wrinkled paper. "

  def do(self, player, command):
    if command=='do test'or command=='do math test'or command=='test'or command=='do problem':
      print('5x3x6=')
      prob1=input()
      if int(prob1)==90:
        print("100%")
      else:
        print("Incorrect!")
        return True
      return False

  def is_named(self, name):
    return name == 'math problem' or 'Math Problem'
  
