from math import *
def cartToSpher(x,y,z):
    return sqrt(x**2+y**2+z**2),atan(z/sqrt(x**2+y**2+z**2)),atan(y/x)