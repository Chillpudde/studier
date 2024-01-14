# Oppgave 2.06: Mindre og storre

x = input("Sjekk om tallet er hoyere eller lavere enn 20: ")

if (x > 10 and x < 20):
    print "Tallet er mellom 10 og 20."
elif (x == 20):
    print "Tallet er lik 20."
elif (x == 10):
    print "Tallet er lik 10."
elif (x < 10):
    print "Tallet er mindre enn 10."
else:
    print "Tallet er storre enn 20."
