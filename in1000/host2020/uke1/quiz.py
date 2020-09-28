# 01.10: Quiz

print("Hva heter hovedstaden i Marokko?: ")

korrekt_svar_1 = "Rabat"
brukersvar_1 = input()

# Bruker metoden ".lower()" for å unngå trøbbel med stor og liten bokstav
if brukersvar_1.lower() == korrekt_svar_1.lower():
    print("Helt rett!")
else:
    print("Beklager, svaret var", korrekt_svar_1)
