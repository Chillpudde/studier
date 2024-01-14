# 02.18: Handletur

brod = 20
melk = 15
ost = 40
yoghurt = 12

sum = 0

print("Velkommen til IFI-butikken \n")

ant_brod = int(input("Hvor mange brød vil du ha?: "))
sum += ant_brod*brod

ant_melk = int(input("Hvor mange kartonger melk vil du ha?: "))
sum += ant_melk*melk

ant_ost = int(input("Hvor mange pakker ost vil du ha?: "))
sum += ant_ost*ost

ant_yoghurt = int(input("Hvor mange pakker yoghurt vil du ha?: "))
sum += ant_yoghurt*yoghurt

print("Du må betale: %1d KR" % (sum))
