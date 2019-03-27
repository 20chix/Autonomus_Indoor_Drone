#!/usr/bin/env python
""" For more info on the documentation go to https://www.decawave.com/sites/default/files/dwm1001-api-guide.pdf
"""

__author__     = "Hadi Elmekawi"
__version__    = "1.0"
__maintainer__ = "Hadi Elmekawi"
__email__      = "w1530819@my.westminster.ac.uk"
__status__     = "Development"

class Anchor:

  def __init__(self, id ,x ,y ,z, distanceFromTag):
    self.id = id
    self.x = x
    self.y = y
    self.z = z
    self.distanceFromTag = distanceFromTag