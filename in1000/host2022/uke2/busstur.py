# 02.20: Busstur

seter = 30
passasjerer = 0

stopp1 = int(input("Stopp 1! Hvor mange går på?: "))

if (seter > 0 and passasjerer <= seter):
    seter -= passasjerer
    passasjerer += stopp1
    
    print("%.1d passasjerer gikk på bussen. \n" % (stopp1))

else:
    stopp1 = abs(seter-stopp1)
    seter -= stopp1

    print("Bussen er full! %.1d fikk gå på bussen." % (stopp1))

stopp2 = int(input("Stopp 2! Hvor mange går på?: "))

if (seter > 0 and passasjerer <= seter):
    seter -= passasjerer
    passasjerer += stopp2

    print("%.1d passasjerer gikk på bussen. \n" % (stopp2))

else:
    stopp2 = seter
    seter -= stopp2

    print("Bussen er full! %.1d fikk gå på bussen." % (stopp2))


stopp3 = int(input("Stopp 3! Hvor mange går på?: "))

if (seter > 0 and passasjerer <= seter):
    seter -= passasjerer
    passasjerer += stopp3

    print("%.1d passasjerer gikk på bussen. \n" % (stopp3))

else:
    stopp3 = seter
    seter -= stopp3

    print("Bussen er full! %.1d fikk gå på bussen." % (stopp3))


print("%.1d ble med til siste stopp." % (passasjerer))