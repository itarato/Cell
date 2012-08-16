import meta

class CellStage:
  G0 = 0
  G1 = 1
  S  = 2
  G2 = 3
  M  = 4

class CellDivisionMember:
  MASTER = 0
  CHILD  = 1

class CellType:
  GENERAL = 0

@meta.autoincrement
@meta.selfcollector
class Cell(object):

  dna = None

  type = CellType.GENERAL

  stage = CellStage.G0
  stageProgress = 0 # 0 - 1

  """
  Constructor shouldn't be called directly. A cell cannot be just created.
  """
  def __init__(self, dna = None, type = CellType.GENERAL):
    super(Cell, self).__init__()

    # Count.
    self.serial = self.__class__.serial
    self.__class__.serial += 1

    # Add to the collections.
    self.__class__.instances.append(self)

    # Genetic information.
    self.dna = dna
    self.type = type

  def __repr__(self):
    return 'Cell %d:\nType: %s\nStage: %s\n' % \
    (
      self.serial,
      self.type,
      self.stage
    )

  def __str__(self):
    return '<%s [%d]>' % (self.__class__.__name__, self.serial)

  def reactOnTime(self):
    if self.stage == CellStage.G0:
      self.stage = CellStage.G1
    elif self.stage == CellStage.G1:
      self.stage = CellStage.S
    elif self.stage == CellStage.S:
      self.stage = CellStage.G2
    elif self.stage == CellStage.G2:
      self.stage = CellStage.M
    else:
      Cell()
      self.stage = CellStage.G0