# 02.19: Utskrift av sirkelberegning

import math

radius = float(input("Skriv inn radius: "))

diameter = radius*2
areal = math.pi*radius**2
omkrets = math.pi*diameter

f_diameter = "{:.2f}".format(diameter)
f_areal = "{:.2f}".format(areal)
f_omkrets = "{:.2f}".format(omkrets)

#
print("Diameteren: {n1:>7}".format(n1 = f_diameter))
print("Arealet: {n2:>10}".format(n2 = f_areal))
print("Omkretsen: {n3:>8}".format(n3 = f_omkrets))

# eller
"""
print("Diameter: % 9.2f" % diameter)
print("Areal: % 12.2f"  % areal)
print("Omkrets: % 10.2f" % omkrets)
"""
