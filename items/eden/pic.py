from item import Item

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> origin/master
=======
>>>>>>> origin/master
=======
>>>>>>> origin/master
class Pic(Item):
    def __init__(self):
        self.id = 'Pic'
        self.name = 'a picture of wizard elements'
        self.description = 'a picture of wizard elements'
        self.can_be_taken = True

    def is_named(self, name):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        return name == 'pic'
=======
        #return name == 'pic'
        return name in ['pic', 'picture']
>>>>>>> origin/master
=======
        #return name == 'pic'
        return name in ['pic', 'picture']
>>>>>>> origin/master
=======
        #return name == 'pic'
        return name in ['pic', 'picture']
>>>>>>> origin/master

    def do(self,player,command):
      if command=='take pic':
        print('You study the pic, and then put it on the table.')
