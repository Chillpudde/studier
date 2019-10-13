# Oppgave 3: Problemløsning med beslutninger


def set_dato(): # Setter dato, og sjekker gyldighet
    dato = [int(input("\nDag: ")), int(input("Mnd: "))]

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
        print("Riktig rekkefølge!")
    elif dato1 == dato2:
        print("Samme dato!")
    else:
        print("Feil rekkefølge!")


print("Datoene skal skrives inn i stigende rekkefølge")

print("\nSkriv inn dato 1 (dd.mm): ")
dato1 = set_dato()
print("\nSkriv inn dato 2 (dd.mm): ")
dato2 = set_dato()

print("\nDato 1: ", end='')
print(*dato1, sep=".")

print("\nDato 2: ", end='')
print(*dato2, sep=".")

sjekk_rekkefolge(dato1, dato2)


""" TO DO:
Frivillig: Skriv et nytt program i
filen dato2.py som gjør det samme som i punkt 2, men
der brukeren skal skrive hver dato som ett heltall i stedet for to.
Gi brukeren eksempel på hvordan datoen bør skrives for å sikre at
sammenligningen i programmet ditt kan gjøres enklere enn i punkt 2"""
