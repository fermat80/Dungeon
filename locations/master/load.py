from .house import Foyer
from .house import GameRoom
from .house import EasyChallengeRoom
from .house import MediumChallengeRoom
from .house import HardChallengeRoom
from .house import ChallengeArea

def locations():
  return [Foyer(), GameRoom(), EasyChallengeRoom(), MediumChallengeRoom(), HardChallengeRoom(), ChallengeArea()]