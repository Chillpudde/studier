# 03.08: Feil som ikke gir feilmelding

"""
x = 0
y = 0

x = int(input("Tast inn et heltall: "))
x = int(input("Tast inn et heltall til: "))

print("Summen av tallene er:", x+y)
"""

# Her er feilen av variabelen "x" endrer verdi i linje 7. Korrekt kode nedenfor:

x = 0
y = 0

x = int(input("Tast inn et heltall: "))
y = int(input("Tast inn et heltall til: "))

print("Summen av tallene er:", x + y)
