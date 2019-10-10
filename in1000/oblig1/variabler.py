# IN1000: Obligatorisk innlevering 1

# Oppgave 1: Utskrift og innlesing med variabler

# 1. OK, se filnavn

# 2.
print("Hei Student!")

# 3. - 7.
navn = input()
print("Hei", navn)

a = 5
b = 2

print(a)
print(b)

beregn_diff = a-b

print("Differanse:", beregn_diff)

nytt_navn = input()

sammen = [navn, "og", nytt_navn]

print(' '.join(map(str, sammen)))
