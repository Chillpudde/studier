# 03.15: Feil i program

navn = input("Hva heter du? ")
alder = int(input("Hva er ditt alder? ")) # må gjøre om til int


print("Hei, " + navn + ", fint navn!") # manglet "+" før og etter "navn"


foerste_bokstav = navn[0]

if foerste_bokstav == "P": # tester boolian verdi med dobbel "=", fjernet et "="
    print("Navnet ditt starter med P, som Python!")
else:
    print("Jeg kjenner ingen ord som starter med", foerste_bokstav)


alder_i_fem_aar = alder + 5

print("Om fem aar vil du vaere", alder_i_fem_aar) #endret æ og å


if alder >= 18:
    if alder < 100:
        drikke = "ol"
    else:
        drikke = "livets eliksir"
else:
    drikke = "brus" # brus er ingen variabel, men tekst. Mangler ""


print("Hei, " + navn + ", har du lyst paa " + drikke + "?")
# ingen variabel "name", endrer til navn
