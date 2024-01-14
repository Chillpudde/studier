# Oppgave 3: Billettpris

def beregn_billettpris():
    alder = int(input("Skriv inn alder: "))
    billettpris = 0 # kr

    if (alder <= 17):
        billettpris = 30
    elif (alder > 17 and alder < 63):
        billettpris = 50
    else:
        billettpris = 35
    return billettpris

def kunde_type(pris):
    kundeklasse = "NONE"

    if (pris <= 17):
        kundeklasse = "barn"
    elif (pris > 17 and pris < 63):
        kundeklasse = "voksen"
    else:
        kundeklasse = "senior"
    return kundeklasse

pris = beregn_billettpris()
kunde = kunde_type(pris)

print("Billettprisen er", pris, "kr for", kunde)
