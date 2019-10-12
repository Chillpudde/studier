# Oppgave 2: Beslutninger

print("Vil du ha en brus? (ja/nei): ")

svar = input().upper().lower()

if svar == "ja":
    print("Her har du en brus!")
elif svar == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt.")
