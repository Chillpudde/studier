# 1.09: Utskrift av sirkelberegning

import math

radius = 9
diameter = 2*radius

def omkrets(diameter):
    o = math.pi*diameter
    return round(o, 2)

def areal(radius):
    a = math.pi*radius**2
    return round(a, 2)

print ' Diameter: ', diameter, '\n Areal: ', areal(radius), '\n Omkrets: ', omkrets(diameter)
