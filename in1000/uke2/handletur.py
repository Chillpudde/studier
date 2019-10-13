# 2.09: Handletur

print("\nHei! Velkommen til IFI-butikken.\n")
pris_brod = 20
pris_melk = 15
pris_ost = 40
pris_youghurt = 12

ant_brod = int(input("Hvor mange brød vil du ha?: "))
ant_melk = int(input("Hvor mange melk vil du ha?: "))
ant_ost = int(input("Hvor mange ost vil du ha?: "))
ant_youghurt = int(input("Hvor mange youghurt vil du ha?: "))

pris = ant_brod*20 + ant_melk*15 + ant_ost*40 + ant_youghurt*12

print(f'Du skal betale {pris} kr.')
