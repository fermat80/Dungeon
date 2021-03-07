from item import Item

class EasyChallengeBadge(Item):

  def __init__(self):
    self.id = 'master_easychallengebadge'
    self.name = 'Easy Challenge Badge'
    self.description = "The easy challenge badge, earned by completing an easy challenge."

  def is_named(self, name):
    return name in ['badge', 'easy badge', 'easy challenge badge']
