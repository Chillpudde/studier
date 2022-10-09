# 01.16 Enda flere beslutninger

# a)
a = 6
b = 5

if a + b > 11:
    print("IN1000")
# a + b = 11. Ikke større enn 11, skrives ikke ut.

# b)
if 1 == 1 and 2 > 3:
    print("IN1000")
# 1 er lik 1, men 2 er ikke større enn 3. Skrives ikke ut. Begge må være true

# c)
if 1 < 2 or 2 < 1:
    print("IN1000")
# Holder at en av dem er true. 1 er mindre enn 2. Skrives ut.

# d)
if 3 < 2:
    print("IN1000")
elif 4 + 2 == 6:
    print("IN1000")
else:
    print("ingenting")
# 3 er større enn 2, IN1000 printes ikke ut
# 4 + 2 er lik 6, IN1000 printes ut
# når aldri else, da foregående statement er true

# e)
a = "b"
b = 3

if 1 == 2:
    if "a" == a:
        print("IN1000")
    else:
        print("ingenting")
else:
    if 1 > 2 or 1 < 2:
        if b >= 3:
            print("IN1000")
        else:
            print("ingenting")
    else:
        print("ingenting")
"""
1 == 2 er false, går aldri videre. Går rett til else
1 er ikke større enn 2, men 1 er mindre enn 2, går til neste
Variabel b er større enn eller lik 3, "IN1000" skrives ut
Stopper her, går ikke videre
"""
