from item import Item


class Pic():
    def __init__(self):
        self.id = 'Pic'
        self.name = 'a picture of wizard elements'
        self.description = 'a picture of wizard elements'
        self.can_be_taken = True

    def is_named(self, name):
        return name == 'Pic'

    def do(self,player,command):
      if command=='take pic':
        print('You study the pic, and then put it back on the wall.')