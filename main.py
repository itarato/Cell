'''
Cell simulation.
'''

from cell import Cell

def simpleInstatiationSimulation():
  for i in range(7): print((Cell()).__repr__)

  # print(Cell.instances)

if __name__ == '__main__':
  print("Cell simulation")

  simpleInstatiationSimulation()
