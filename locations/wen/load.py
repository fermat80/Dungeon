from .library import Library
from .library import BookShelf
from .library import Flash_light

def locations():
  return [Library(), BookShelf(), Flash_light()]
  #return [Library(), BookShelf()]