# 01.18 Største verdi

a = int(input("Tall 1: "))
b = int(input("Tall 2: "))
c = int(input("Tall 3: "))
big_v = 0
ant_big_v = 0

if(a >= b and a >= c):
    big_v = a
    ant_big_v += 1
if(b >= a and b >= c):
    big_v = b
    ant_big_v += 1
if(c >= a and c >= b):
    big_v = c
    ant_big_v += 1

print("Største verdien er:", big_v)

if(ant_big_v == 1):
    print("Det er kun ett tall som er størst.")
else:
    print(ant_big_v,"av tallene er lik den storste verdien.")
