# Oppgave 4: Kodeforståelse og feilsøking

"""
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
print (b + "Hei!")
"""

# 1. Er dette lovlig kode? Begrunn svaret.
"""
Nei, dette er ikke lovlig kode.
"""

# 2. Hvilke problemer vil vi kunne møte på når vi kjører denne koden?
"""
Problem 1:
    I første linje ber vi bruker legge inn et heltall, i andre linje
    konverteres a til et heltall, i tredje linje forsøker vi å sjekke om b er
    mindre enn 10. Dersom b er mindre enn 10 skal programmet skrive ut b +
    teksten "Hei!". Om dette er tilfellet møter vi på feilen. Da a ikke lenger
    er en string, men en integer så kan ikke verdiene av variablene legges
    sammen. Om man ikke hadde konvertert a i andre linje ville resultatet
    blitt: (det bruker skrev inn)Hei!
    Dersom b er lik eller større enn 10 kjører programmet fint. (Sett at man
    har innrykk i fjerde linje)

Problem 2:
    Fjerde linje er utenfor scope'et til if-testen.
"""

# FIXED
a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b, "Hei!")
