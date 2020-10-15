# 02.08: kroppstemperatur

temp_L = 36.5
temp_H = 37.5

print("| Har du feber? |")
temperatur = float(input("Har du feber? Skriv inn din kroppstemperatur: "))

if (temperatur < temp_L):
    print("Din kroppstemperatur er under normal kroppstemperatur.")
elif (temperatur > temp_H):
    print("Din kroppstemperatur er over normal kroppstemperatur.")
else:
    print("Din kroppstemperatur er normal.")
