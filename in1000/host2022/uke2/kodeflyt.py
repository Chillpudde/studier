# 02.11: Kodeflyt

pris = 50
tekst = input("Skriv inn alder: ")
alder = int(tekst)

if alder < 12 or alder > 67:
    print("Du må betale", pris*0.5, "kr")
else:
    print("Du må betale", pris, "kr")

print("ha en fin dag!")

"""
a) Hvis bruker taster inn 50:
linje 3 --> l4 --> l5 --> l7 --> l9 --l10 --> l12

b) Hvis bruker taster inn 80:
linje 3 --> l4 --> l5 --> l7 --> l8 --> l12

c) Hvis bruker taster inn 12
linje 3 --> l4 --> l5 --> l7 --> l9 --l10 --> l12, samme som a)
