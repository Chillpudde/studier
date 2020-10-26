# 02.21: Finn ut om siste siffer er felles

a = 3456
b = 10
c = 666

if (a%10 == b%10):
    print(f"Siste siffer i {a} og {b} er like.")
if (a%10 == c%10):
    print(f"Siste siffer i {a} og {c} er like.")
if (b%10 == c%10):
    print(f"Siste siffer i {b} og {c} er like.")
