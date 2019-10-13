# 2.03: Utskrift av sirkelberegning

import math

radius = float(input("\nSkriv inn sirkelens radius: "))

diameter = 2*radius
areal = math.pi*radius**2
omkrets = diameter*math.pi

print("\nDiameter: {0:.2f}".format(diameter))
print("Areal:    {0:.2f}".format(areal))
print("Omkrets:  {0:.2f}".format(omkrets))
