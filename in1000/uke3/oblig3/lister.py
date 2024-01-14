# Oppgave 1: Lister

# 1.
liste_1 = [69, 666, 420]
print(liste_1[0], liste_1[2])

# 2.
liste_2 = []

navn_1 = input("Skriv inn navn 1: ")
liste_2.append(navn_1.lower())
navn_2 = input("Skriv inn navn 2: ")
liste_2.append(navn_2.lower())
navn_3 = input("Skriv inn navn 3: ")
liste_2.append(navn_3.lower())
navn_4 = input("Skriv inn navn 4: ")
liste_2.append(navn_4.lower())

# 3.
if ("andreas" in liste_2):
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# 4.
sum = 0
produkt = 1
teller = 0
liste_3 = []

for tall in liste_1:
    sum += liste_1[teller]
    produkt *= liste_1[teller]
    teller += 1
teller = 0

print(sum, produkt)
liste_3.append(sum)
liste_3.append(produkt)

liste_4 = []

for tall in liste_1:
    liste_4.append(liste_1[teller])
    teller += 1

teller = 0
for tall in liste_3:
    liste_4.append(liste_3[teller])
    teller += 1

print(*liste_4)

liste_4.pop(4)
liste_4.pop(3)

print(*liste_4)
