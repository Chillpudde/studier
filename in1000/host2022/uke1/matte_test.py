# 01.15 test matte

print("Hva er 2 + 3?: ")
svar_1 = int(input())
fasit_1 = 5

if(svar_1 != fasit_1):
    print("du tapte!")
    exit()

print("Hva er 4 * 4?: ")
svar_2 = int(input())
fasit_2 = 16

if(svar_2 != fasit_2):
    print("du tapte")
    exit()

print("Hva er 2^3?: ")
svar_3 = int(input())
fasit_3 = 8

if(svar_3 != fasit_3):
    print("du tapte!")
    exit()
else:
    print("du vant!")

# fasiten sier:
"""
svar = input("1 + 1 = ")

if svar == "2":
    svar = input("5 * 4 = ")

    if svar == "20":
        svar = input("10 / 2 = ")

        if svar == "5":
            print("du vant!")
        else:
            print("du tapte!")
    else:
        print("du tapte!")
else:
    print("du tapte!")
"""
# Begge deler fungerer
