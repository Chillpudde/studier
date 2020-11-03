# Oppgave 5: Egen Oppgave
# Filnavn: min_oppgave.py

"""
Oppgave: Lag en quiz som stiller spørsmål til bruker og gir tilbakemelding på
    om svarene er korrekte.
"""

print("*QUIZ*")

spm_1 = input("1. Hvor mange dager er det i et skuddaar?: ")
if (spm_1 == "366"):
    print("KORREKT!")
else:
    print("FEIL!")

spm_2 = input("2. Hvem var president i USA fra 2016-2020? (Etternavn): ")
if (spm_2 == "Trump"):
    print("KORREKT!")
else:
    print("FEIL!")

spm_3 = input("Hva er mitt favoritt-ol: ")
if (spm_3 == "Guinness"):
    print("KORREKT!")
else:
    print("FEIL!")

"""
I dette programmet er det mye som kan forbedres. Catcher ikke lower/upper case,
kunne gitt svaralternativer, flere spørsmål, etc... #latskap
"""
