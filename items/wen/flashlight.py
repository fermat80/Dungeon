from item import Item


class Flashlight(Item):

  is_FlashlightOn = False

  def __init__(self):

    # These are required for all items...
    self.id = 'Flashlight'
    self.name = 'A Flashlight'
    self.description = 'A magic Flashlight'

  # Single words that allow us to look at or take this object...
  def is_named(self, name):
    return name == 'flashlight'

  def is_FlashlightOn(self):
    return self.is_FlashlightOn; 
  # This is optional!  But allows you to add code when creating the description.
  # You could also simply change self.description.  See below how we do this with
  # self.name.
  def get_description(self):
    if self.is_FlashlightOn:
      return self.description + ' The Flashlight is on!'
    return self.description + ' The Flashlight is off!'
  
  def do(self, player, command):
    if self.is_my_command(command, 'turn on'): # command == 'turn on':      
      if not self.is_FlashlightOn:
        print('You turn on the Flashlight to see things around you.')
        self.name = 'A Flashlight.'
        self.is_FlashlightOn = True
        return True
      else:
        print('Flashlight is already turned on.')
        self.name = 'A Flashlight.'
        self.is_FlashlightOn = True
        return True
    if command == 'turn off':      
      if not self.is_FlashlightOn:
        print('Flashlight is already turned off.')
        self.name = 'A Flashlight.'
        self.is_FlashlightOn = False
        return True
      else:
        print('You turn off the Flashlight to go back to darkness.')
        self.name = 'A Flashlight.'
        self.is_FlashlightOn = False
        return True
