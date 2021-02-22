from item import Item

class Note1(Item):

  def __init__(self):
    self.id = 'Michael.Note1'

    self.name = 'Note'

    self.description = " You examine the note. It seems to be for somebody. Some parts of the note are worn down, making them unreadable. It seems to be part of a notebook. You can read it."

  def do(self, player, command):
    if command == 'read note' or command=='read':

      message = """There are dang rs.ȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ You mus  watch your step.ȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ Thin s h ve gone t rribly wro g. Wat h ou  for thȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ 
      """

      print(message)
      return True      
    return False

  def is_named(self, name):
    return name == 'note1'

class Note2(Item):

  def __init__(self):
    self.id = 'Michael.Note2'

    self.name = 'Note'

    self.description = " You examine the note. It seems to be for somebody. The note is in fair condition, but is ripped off at one part. It seems to be part of a notebook. You can read it."

  def do(self, player, command):
    if command == 'read note' or command=='read':

      message = """ Nothing in my life could have prepared me for this. I hope that you will be prepared for what comes. Sometimes I feel time flies, but others times time ticks by very slowly. But keep track of time, because midnight shall be of significance. I hope you are luckier than I am."""


      print(message)
      print("You quickly realize there are dangers, yet there is still hope. ")
      return True      
    return False

  def is_named(self, name):
    return name == 'note2'