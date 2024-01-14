# 02.08: Kroppstemperatur

temp_low = 36.5
temp_high = 37.5
user_temp = float(input("Din kroppstemperatur: "))

if (user_temp < temp_low):
    print("Under normal kroppstemperatur")
elif(user_temp > temp_high):
    print("Over normal kroppstemperatur.")
else:
    print("Normal kroppstemperatur.")
