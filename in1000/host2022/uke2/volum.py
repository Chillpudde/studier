# 02.13: Volum med feil

"""
Finn tre feil

lengde = 3 | OK
bredde = 5 | OK
volum = lengde * bredde * høyde | mangler variabel "høyde"
Print("Volumet er:" + volum) | print, ikke Print | Kan ikke addere str og int (volum)
"""

lengde = 3
bredde = 5
hoyde = 8

volum = lengde * bredde * hoyde
print("Volumet er: ", volum)