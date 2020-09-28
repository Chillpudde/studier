# Opgave 1. Utskriftsprosedyre #

# 1.
navn = input("Skriv inn navn: ")
sted = input("Hvor kommer du fra? ")

print("Hei, " + navn + "! Du er fra " + sted + ".")

# 2.
count = 0
while count < 3:
    navn = input("\n" + "Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")

    print("Hei, " + navn + "! Du er fra " + sted + ".")
    count = count+1
