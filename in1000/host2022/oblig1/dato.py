# Oppgave 3: Problemløsning med beslutninger

print("Skriv inn en dato 1(dd.mm): ")
dag1 = input("Dag: ")
mnd1 = input("Måned: ")
print("Dato 1: ", dag1 + "." + mnd1)

print("Skriv inn en dato 2(dd.mm): ")
dag2 = input("Dag: ")
mnd2 = input("Måned: ")
print("Dato 2: ", dag2 + "." + mnd2)

if(mnd1 <= mnd2 and dag1 < dag2):
    print("Riktig rekkefølge!")
elif(mnd1 >= mnd2 and dag1 > dag2):
    print("Feil rekkefølge!")
else:
    print("Samme dato!")
