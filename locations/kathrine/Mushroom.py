from location import Location
from items.kathrine.coat import Coat
from items.kathrine.newspaper import Newspaper
from items.kathrine.math import Math
from items.kathrine.master_keys import TwoSumKey
from items.kathrine.master_keys import ShuffleKey
from items.kathrine.master_keys import ShuffleKey2
from items.master.badges import EasyChallengeBadge

class FairyHouse(Location):

  def __init__(self):

    self.id = 'fairy_house'
    self.name = 'Fairy House'
    self.description = 'You are in a fairy house. That means you are in an oversized mushroom. The mushroom is bright red. It is not poisonous.'
    self.contents = [Newspaper(), Coat(), Math(), TwoSumKey(), ShuffleKey(), EasyChallengeBadge(1), ShuffleKey2()]