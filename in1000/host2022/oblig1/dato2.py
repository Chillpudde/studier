# Oppgave 3: Problemløsning med beslutninger (Frivillig)

# Første dato
print("Skriv inn en dato 1(dd.mm): ")
dato1 = input("Dato 1: ").split(".")

dag1 = int(0)
if(int((dato1[0])[0]) == 0):
    dag1 = int(((dato1[0])[1]))
else:
    dag1 = int(dato1[0])

mnd1 = int(0)
if(int((dato1[1])[0]) == 0):
    mnd1 = int(((dato1[1])[1]))
else:
    mnd1 = int(dato1[1])

if(int((dato1[0])[0]) == 0) and (int((dato1[1])[0]) == 0):
    dato_format1 = "Dato 1 er: 0{}.0{}".format(dag1,mnd1)
    print(dato_format1)
elif(int((dato1[0])[0]) != 0) and (int((dato1[1])[0]) == 0):
    dato_format1 = "Dato 1 er: {}.0{}".format(dag1,mnd1)
    print(dato_format1)
elif(int((dato1[0])[0]) == 0) and (int((dato1[1])[0]) != 0):
    dato_format1 = "Dato 1 er: 0{}.{}".format(dag1,mnd1)
    print(dato_format1)
else:
    dato_format1 = "Dato 1 er: {}.{}".format(dag1,mnd1)
    print(dato_format1)

# Andre dato
print("Skriv inn en dato 2(dd.mm): ")
dato2 = input("Dato 2: ").split(".")

dag2 = int(0)
if(int((dato2[0])[0]) == 0):
    dag2 = int(((dato2[0])[1]))
else:
    dag2 = int(dato2[0])

mnd2 = int(0)
if(int((dato2[1])[0]) == 0):
    mnd2 = int(((dato2[1])[1]))
else:
    mnd2 = int(dato2[1])

if(int((dato2[0])[0]) == 0) and (int((dato2[1])[0]) == 0):
    dato_format2 = "Dato 2 er: 0{}.0{}".format(dag2,mnd2)
    print(dato_format2)
elif(int((dato2[0])[0]) != 0) and (int((dato2[1])[0]) == 0):
    dato_format2 = "Dato 2 er: {}.0{}".format(dag2,mnd2)
    print(dato_format2)
elif(int((dato2[0])[0]) == 0) and (int((dato2[1])[0]) != 0):
    dato_format2 = "Dato 2 er: 0{}.{}".format(dag2,mnd2)
    print(dato_format2)
else:
    dato_format2 = "Dato 2 er: {}.{}".format(dag2,mnd2)
    print(dato_format2)

# Check
if((dag1 < dag2 and mnd1 <= mnd2) or (dag1 > dag2 and mnd1 < mnd2)):
    print("Riktig rekkefølge!")
elif(dag1 >= dag2 and mnd1 > mnd2):
    print("Feil rekkefølge!")
else:
    print("Samme dato!")
