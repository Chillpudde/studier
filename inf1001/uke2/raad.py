# Oppgave 2.13: Har du raad?

saldo_inn = input("Tast inn saldo: ")
saldo = float(saldo_inn)

varepris_inn = input("Hvor mye koster varen?: ")
varepris = float(varepris_inn)

if (saldo >= varepris):
    print "Du har raad"
else:
    print "Du har ikke raad"
