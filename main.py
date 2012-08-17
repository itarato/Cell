'''
Cell simulation.
'''

from threading import Thread
from cell import Cell
from cell import iterateCulture
import time


class CellProliferationThread(Thread):

  def __init__(self):
    super(CellProliferationThread, self).__init__()

  def run(self):
    origin_cell = Cell()
    while True:
      iterateCulture()



def simpleInstatiationSimulation():
  c = Cell()
  print(c)
  print(c.__repr__)

def cellProliferation():
  try:
    cellProliferationThread = CellProliferationThread()
    cellProliferationThread.daemon = True
    cellProliferationThread.start()
    while True:
      time.sleep(100)
      # Tick.
      print('.')
  except (KeyboardInterrupt, SystemExit):
    print('End of cell proliferation')
    raise
  except:
    pass

'''
Entry point.
'''
if __name__ == '__main__':
  print("Cell simulation")

  # simpleInstatiationSimulation()
  cellProliferation()
