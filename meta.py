"""
Count instances.
"""
def autoincrement(_class):
  _class.serial = 0
  return _class