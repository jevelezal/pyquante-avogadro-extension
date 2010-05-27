#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart ")

import matplotlib
def f3d(x,y,z):
    return x**2 + y**2 + z**2 - 25
help(matplotlib)
from matplotlib import pyplot as pl
#?pl.contour
import numpy
grid = numpy.ogrid[-10:10:50j, -10:10:50j, -10:10:50j]
scalars = f3d(grid)
scalars = f3d(*grid)
pl.contour(scalars)
pl.contour(scalars, [0.1,0.2,0.3])
pl.contourf(scalars, [0.1,0.2,0.3])
pl.contour([0.1,0.2,0.3])
scalars.shape()
scalars.shape
scalars[0].shape
pl.contour(scalars[0])
pl.show()
