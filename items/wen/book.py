from item import Item

class Book(Item):

  def __init__(self):

    # These are required for all items...
    self.id = 'spells_book'
    self.name = 'A book'
    self.description = 'A strange magic book of spells'

    # This is an extra variable that we will use to keep track of our status.
    self.is_bookOpened = False

  # Single words that allow us to look at or take this object...
  def is_named(self, name):
    return name == 'book'
    
  # This is optional!  But allows you to add code when creating the description.
  # You could also simply change self.description.  See below how we do this with
  # self.name.
  def get_description(self):
    if self.is_bookOpened:
      return self.description + ' The book is opened!'
    return self.description + ' The book is closed!'
  
  def do(self, player, command):
    if command == 'open book':      
      if not self.is_bookOpened:
        print('You open the book to see the spells.')
        self.name = 'A book with spells.'
        self.is_bookOpened = True
      else:
        print('You close the book to undo the spells.')
        self.name = 'A book.'
        self.is_bookOpened = False
      return True

