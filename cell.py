import meta

class CellStage:
  G0 = 0
  G1 = 1
  S  = 2
  G2 = 3
  M  = 4

class CellType:
  GENERAL = 0

@meta.autoincrement
@meta.selfcollector
class Cell(object):

  dna = None

  type = CellType.GENERAL

  stage = CellStage.G0

  """
  Constructor shouldn't be called directly. A cell cannot be just created.
  """
  def __init__(self):
    super(Cell, self).__init__()

    # Count.
    self.serial = self.__class__.serial
    self.__class__.serial += 1

    # Add to the collections.
    self.__class__.instances.append(self)

  def __repr__(self):
    return 'Cell %d:\nType: %s\nStage: %s\n' % \
    (
      self.serial,
      self.type,
      self.stage
    )

  def __str__(self):
    return '<%s [%d]>' % (self.__class__.__name__, self.serial)
