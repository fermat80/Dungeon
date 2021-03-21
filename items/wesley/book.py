from item import Item 

class Book(item):

  def_init_(self):

    self.id = 'wesley_book'
    self.name = 'A book'
    self.descirption = 'A book covered with ash'


    self.is_locked = True

    def is_named(self, name):
      return name == 'book'

    def do(self, player, command):
        if command == 'open book':
          if not self.is_locked:
            print('The book is unlocked.')
  