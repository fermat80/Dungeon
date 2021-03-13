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
<<<<<<< HEAD
        return True

      return False
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return True
      return False
        
>>>>>>> origin/master

=======
      return True
      
    return False
>>>>>>> origin/master
=======
      return True
      
    return False
>>>>>>> origin/master
=======
      return True
      
    return False
>>>>>>> origin/master

  def is_named(self, name):
    return name == 'math problem' or 'Math Problem'
  
