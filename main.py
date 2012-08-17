'''
Cell simulation.
'''

from threading import Thread
from cell import Cell
import time


class CellProliferationThread(Thread):

  def __init__(self):
    super(CellProliferationThread, self).__init__()

  def run(self):
    origin_cell = Cell()
    while True:
      Cell.iterateCulture()



def simpleInstatiationSimulation():
  c = Cell()
  print(c)
  print(c.__repr__)

def timeLapse():
  while True:
    pass

if __name__ == '__main__':
  print("Cell simulation")

  simpleInstatiationSimulation()
  # timeLapse()
