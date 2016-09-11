# Oppgave 2.12: Busstur

PLASSER = 30
passasjerer = 0
counter = 0

for x in xrange(0, 3):
    passasjer_inn = input("Hvor mange gaar paa?: ")
    passasjerer = passasjerer + passasjer_inn
    counter += 1
    
    if (passasjerer >= PLASSER):
        print "Bussen er full"
        if (passasjerer > PLASSER):
            print passasjerer - PLASSER, "maatte gaa."
        break

    if (passasjerer <= PLASSER and counter == 3):
        print "Alle fikk plass!"
