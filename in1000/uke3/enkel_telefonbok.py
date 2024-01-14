# 03.11: Enkel telefonbok

dictionary = {}

dictionary["Arne"] = 22334455
dictionary["Lisa"] = 95959595
dictionary["Jonas"] = 97959795
dictionary["Peder"] = 12345678

valg = input("Skriv inn et navn: ")

if valg in dictionary:
    print("Telefonnummeret er:", dictionary[valg])
else:
    print("Ugyldig valg!")
