# 03.05: Bakeri

bakeri = {}

bakeri["Croissant"] = 25
bakeri["Grovbroed"] = 40
bakeri["Kneipbroed"] = 20
bakeri["Rosinbolle"] = 20
bakeri["Baguette"] = 10

"""
print("MENY")
for vare in bakeri:
    print(vare + ": " + str(bakeri[vare]), "kr")

bakeri["Croissant"] += 10

print("MENY")
for vare in bakeri:
    print(vare + ": " + str(bakeri[vare]), "kr")
"""

def meny(tekst):
    bakeri["Croissant"] += 10
    print("MENY")
    for vare in bakeri: # for <element> in <list>
        print(vare + ": " + str(bakeri[vare]), "kr")

meny(bakeri)
