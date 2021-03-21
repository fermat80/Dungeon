from item import Item

class Note1(Item):

  def __init__(self):
    self.id = 'Michael.Note1'

    self.name = 'Note'

    self.description = " You examine the note. It's written in scrawny black ink and the paper is yellow. You can read it."

  def do(self, player, command):
    if command == 'read note' or command=='read':

      message = """
      ====================
      How did you get here?
      ====================
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

    self.description = " You examine the note. It's written in scrawny black ink and the paper is yellow. You can read it."

  def do(self, player, command):
    if command == 'read note' or command=='read':

      message = """ 
      ============================================================================================
      Please take this as a warning. I advise you to leave, before I have to deal with you myself.
      ============================================================================================
      """


      print(message)
      print("You quickly realize there are dangers, yet there is still hope. ")
      return True      
    return False

  def is_named(self, name):
    return name == 'note2'