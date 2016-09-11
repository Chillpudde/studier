# Oppgave 2.10: Handletur

BROD = 20 #kr
MELK = 15
OST = 40
YOUGHURT = 12

ant_brod = input("Skriv inn antall brod: ")
ant_melk = input("Skriv inn antall melk: ")
ant_ost = input("Skriv inn antall ost: ")
ant_youghurt = input("Skriv inn antall youghurt: ")

tot_sum = ant_brod*BROD + ant_melk*MELK + ant_ost*OST + ant_youghurt*YOUGHURT
print "Handleturen kostet: ", tot_sum, "kr."
