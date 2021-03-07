from .house import Foyer
from .house import GameRoom
from .challenge import EasyChallengeRoom
from .challenge import MediumChallengeRoom
from .challenge import HardChallengeRoom
from .challenge import ChallengeArea
from .challenge import TwoSumCloset

def locations():
  return [
    Foyer(),
    GameRoom(),
    EasyChallengeRoom(),
    MediumChallengeRoom(),
    HardChallengeRoom(),
    ChallengeArea(),
    TwoSumCloset()]