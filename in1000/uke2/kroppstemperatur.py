# 2.08: Kroppstemperatur

temperatur = float(input("Hva er kroppstemperaturen din?: "))

temperatur_min = 36.5
temperatur_max = 37.5

if temperatur < temperatur_min or temperatur > temperatur_max:
    print("Du har unormal kroppstemperaturen.")
else:
    print("du har normal kroppstemperaturen.")
