# Oppgave 3: Problemløsning med beslutninger EXTRA

def set_dato(): # Setter dato, og sjekker gyldighet

    # dato tar nå inn begge både dag og mnd samtidig, separeres med "."
    dato = [int(dato) for dato in input().split(".")]

    max_dag1 = 30
    max_dag2 = 31
    max_dag3 = 28
    max_mnd = 12

    mnd_28 = 2
    mnd_30 = [4, 6, 9, 11]
    mnd_31 = [1, 3, 5, 7, 8, 10, 12]

    check = 0
    while check == 0:
        if dato[0] <= max_dag1 and dato[1] in mnd_30:
            check = 1
            return dato
        elif dato[0] <= max_dag2 and dato[1] in mnd_31:
            check = 1
            return dato
        elif dato[0] <= max_dag3 and dato[1] == mnd_28:
            check = 1
            return dato
        else:
            print("\nIkke gyldig dato, skriv inn en gyldig dato (dd.mm):")
            dato = [int(input("\nDag: ")), int(input("Mnd: "))]

def sjekk_rekkefolge(x, y): # Sjekker rekkefølge på datoer
    if dato1[0] < dato2[0] and dato1[1] <= dato2[1]:
        print("\nRiktig rekkefølge!")
    elif dato1 == dato2:
        print("\nSamme dato!")
    else:
        print("\nFeil rekkefølge!")


print("\nDatoene skal skrives inn i stigende rekkefølge (DD.MM)")

print("\nSkriv inn dato 1: ", end="")
dato1 = set_dato()
print("\nSkriv inn dato 2: ", end="")
dato2 = set_dato()

sjekk_rekkefolge(dato1, dato2)
