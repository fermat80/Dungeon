from .hangman import Hangman
from item import Item

class HangmanGame(Item):

  def __init__(self):
    self.id = 'master_hangman'
    self.name = 'A game of hangman'
    self.description = 'This is the classic game of hangman.  You can "play" it!'

  def do(self, player, command):

    if self.is_my_command(command, 'play'):
      Hangman().play()
      return True

    #if command == 'play hangman' or command == 'play game':
    #  Hangman().play()
    #  return True

    return False

  def is_named(self, name):
    return name == 'hangman' or name == 'game'
