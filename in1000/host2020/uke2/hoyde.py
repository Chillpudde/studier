# 02.10: Høyde

hoyde_L = 140
hoyde_H = 190

hoyde = float(input("Oppgi din hoyde i cm: "))

if (hoyde < 140):
    print("Du er lav.")
elif(hoyde > 190):
    print("Du er hoy.")
else:
    print("Du er middels.")
