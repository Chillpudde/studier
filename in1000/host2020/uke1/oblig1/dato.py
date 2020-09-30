# Oppgave 3: Problemløsning med beslutninger

# 1.
print("Skriv inn to datoer (dag, mnd), i kronologisk rekkefolge \n")

dag_1 = input("Dag: ")
mnd_1 = input("Maaned: ")
dato_1 = dag_1, mnd_1
print(*dato_1, sep = ".")

print("\n")

dag_2 = input("Dag: ")
mnd_2 = input("Maaned: ")
dato_2 = dag_2, mnd_2
print(*dato_2, sep = ".")

# 2.
if (dag_1 < dag_2 and mnd_1 <= mnd_2) or (dag_1 >= dag_2 and mnd_1 < mnd_2):
    print("Riktig rekkefolge!")
elif (mnd_1 > mnd_2) or (mnd_1 == mnd_2 and dag_1 > dag_2):
    print("Feil rekkefolge!")
else:
    print("Samme dato!")
