# Oppgave 2.07: Skatt i Ruritania

inntekt = input("Skriv inn din inntekt: ")
skatt1 = inntekt*0.1
skatt2 = skatt1 + ((inntekt-10000)*0.3)
print (inntekt-10000)*0.3

if (inntekt <= 10000):
    print "Din skatt er: ", skatt1
else:
    print "Din skatt er: ", skatt2
