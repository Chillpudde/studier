# Oppgave 2: Beslutninger

# 1.
brukersvar = input("Vil du ha en brus? (ja/nei): ")

# 2.
"""
".lower()" er en innebygd metode i python for håndtering av tekststrenger.
Den finner alle store bokstaver, og returnerer strengen med kun små bokstaver.
"""

if brukersvar.lower() == "ja":
    print("Her har du en brus!")
elif brukersvar.lower() == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")
