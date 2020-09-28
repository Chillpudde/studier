# Oppgave 1: Utskrift og innlesing med variabler

navn = input("Oppgi et navn: ")
print("Hei,", navn)

x = 5
y = 10

print("\n x:", x, "\n y:", y, "\n")

differanse = x - y
print("Differanse:", differanse)

nytt_navn = input("Oppgi et nytt navn: ")
sammen = navn, nytt_navn

print(*sammen, sep=' og ')
