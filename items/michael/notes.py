class TornNote(Item):

  def __init__(self):
    self.id = 'Michael.Note'

    self.name = 'Note'

    self.description = " You examine the note. Some parts of the note are worn down, making them unreadable. It seems to be part of a bigger note. You can read it."

  def do(self, player, command):
    if command == 'read note' or command=='read TornNote' or command=='read':

      message = """There are dang rs.ȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ You mus  watch your step.ȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ Thin s h ve gone t rribly wro g. Wat h ou  for thȩ̵̷̴̶̸̷̷̵̷̴̷̴̷̸̴̷̶̧̧̢̨̢̢̧̛̛̛͔̪̯̦͚̱͔̗̻̟̫̼̠͓̱͎̟̘͖̫̙̤̭̫̯͚̰̺̤̭̥̠̲͎̤̖͉̬̼̟̯̫̯̠̼̠̤̭͉̬͎͕̙̙̩͉̲̮̳̬͔͈̺̤̗̮̭͉̯̠̱̓̈́͛̃̿̒̄̈́̔̿͂͋̍͑͆̂̀̒̌̅͋̎̾̐̈́͌̽̾̊̍̋̊̐̏̎͐̅̔͛̂͛͆͂̐̒̉̀͗̄̈́̒̈́͗͌͐̓̓͂̆̄̓̆̌͐̓̄̈́̀̌̂̋̉̑̃̽̈́̈̈́͑̋͊̌̄̉́̎̊̚̕͘͘̚̕̕̕͘̚͜͝͝͠͠͝͠͠͝ͅ 

      print(message)
      return True      
    return False

  def is_named(self, name):
    return name == 'note'