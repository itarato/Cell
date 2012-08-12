import meta

@meta.autoincrement
class Cell(object):

  def __init__(self):
    super(Cell, self).__init__()
    self.serial = self.__class__.serial
    self.__class__.serial += 1

  def __str__(self):
    return '<%s [%d]>' % (self.__class__.__name__, self.serial)
