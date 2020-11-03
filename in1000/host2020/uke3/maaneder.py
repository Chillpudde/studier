# 03.03: String-liste med måneder

maaneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli",
    "August", "September", "Oktober", "November", "Desember"]

valg = int(input("Skriv inn et tall (1-12): "))

if (valg > 0 and valg < 13):
    print(maaneder[valg-1])
else:
    print("Ugyldig valg!")
