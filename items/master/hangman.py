import random
from item import Item

class Hangman(Item):

  def __init__(self):
    self.word_list = ['mouse', 'computer', 'street', 'hangman']
    
    self.a = ['   ', ' o ', ' o ', ' o ', ' o ', '\\o ', '\\o/']
    self.b = ['   ', '   ', ' | ', ' | ', ' | ', ' | ', ' | ']
    self.c = ['   ', '   ', '   ', '/  ', '/ \\', '/ \\', '/ \\']

  def play(self):

    #select a secret word...
    secret = random.choice(self.word_list);

    guesses = []
    misses = []
    winner = False

    while len(misses) < 6 and not winner:

      self.fancy_display(secret, guesses, misses)

      letter = self.get_input(guesses)
      
      guesses.append(letter)
      if not letter in secret:
        misses.append(letter)

      winner = True
      for char in secret:
        if not char in guesses:
          winner = False
          
      winner = all([char in guesses for char in secret])

    self.fancy_display(secret, guesses, misses)

    if winner:
      print('\nYou won!')
    else:
      print('\nYou lost!')

  def get_input(self, guesses):
      while True:
        print('next? ', end='')
        letter = input()
        if not letter in guesses:
          break;
      return letter

  def display(self, secret, guesses, misses):

      print('')

      for char in secret:
        if char in guesses:
          print(char + ' ', end='')
        else:
          print('_ ', end='')
      print('')

      #print(' '.join([c if c in guesses else '_' for c in secret]))

      print('Misses: ', end='')
      for char in misses:
        print(char + ' ', end='')
      print('')

      #print('Misses: ' + ' '.join([char for char in misses]))

  def fancy_display(self, secret, guesses, misses):

      miss_count = len(misses)

      print('')

      print(self.a[miss_count] + ' ', end='')

      for char in secret:
        if char in guesses:
          print(char + ' ', end='')
        else:
          print('_ ', end='')
      print('')

      print(self.b[miss_count] + ' ', end='')

      print('Misses: ', end='')
      for char in misses:
        print(char + ' ', end='')
      print('')

      print(self.c[miss_count] + ' ', end='')
