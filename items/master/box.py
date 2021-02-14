from item import Item

class Box(Item):

  def __init__(self):

    # These are required for all items...
    self.id = 'master_box'
    self.name = 'A box'
    self.description = 'A black box with a button that you can "push".'

    # This is an extra variable that we will use to keep track of our status.
    self.is_lit = False

  # Single words that allow us to look at or take this object...
  def is_named(self, name):
    return name == 'box'
    
  # This is optional!  But allows you to add code when creating the description.
  # You could also simply change self.description.  See below how we do this with
  # self.name.
  def get_description(self):
    if self.is_lit:
      return self.description + ' The button is lit!'
    return self.description + ' The button is not lit!'
  
  def do(self, player, command):
    if command == 'push button':      
      if not self.is_lit:
        print('You push the button on the box and the button lights.')
        self.name = 'A box with a lit button.'
        self.is_lit = True
      else:
        print('You push the lit button on the box and the button turns off.')
        self.name = 'A box.'
        self.is_lit = False
      return True

