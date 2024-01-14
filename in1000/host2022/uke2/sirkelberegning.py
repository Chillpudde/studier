# 02.19: Utskrift av sirkelberegning

import math

radius = float(input("Skriv inn radius av sirkel: "))

diameter = radius * 2
areal = math.pi * radius**2
omkrets = math.pi * diameter

print("Diameter: %.2f" % (diameter))
print("Areal: %.2f" % (areal))
print("Omkrets: %.2f" % (omkrets))
