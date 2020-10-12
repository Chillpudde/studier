# Oppgave 3: Problemløsning med beslutninger

# 1.
print("Skriv inn to datoer i kronologisk rekkefolge \n\n")

# Angir antall dager per måned
max_dag_29 = 29
max_dag_30 = 30
max_dag_31 = 31

# Plassholder for datoene som skrives inn
dato_1 = [0,0]
dato_2 = [0,0]

dato_1_input = input("Skriv inn 1. dato:").


print(*dato_1, sep= ".")
print(*dato_2, sep= ".")

# 2.
# a.
if (dato_1[0] < dato_2[0] and dato_1[1] <= dato_2[1]) or (dato_1[0] >= dato_2[0] and dato_1[1] < dato_2[1]):
    print("Riktig rekkefolge!")
# b.
elif (dato_1[1] > dato_2[1]) or(dato_1[1] == dato_2[1] and dato_1[0] > dato_2[0]):
    print("Feil rekkefolge!")
# c.
else:
    print("Samme dato!")
