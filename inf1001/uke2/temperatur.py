# Oppgave 2.08: Kroppstemperatur

inn_temperatur = input("Skriv inn din kroppstemperatur: ")
float_temp = float(inn_temperatur)

if (float_temp < 36.5 or float_temp > 37.5):
    print "Du har feber!"
else:
    print "Du er frisk!"
