# Oppgave 2.11: Hoyde

min_hoyde = 140 #cm
max_hoyde = 190
egen_hoyde = input("Skriv inn din hoyde i cm: ")

if (egen_hoyde < min_hoyde):
    print "Du er lav."
elif (egen_hoyde > max_hoyde):
    print "Du er hoy."
else:
    print "Din hoyde er gjennomsnittlig."
