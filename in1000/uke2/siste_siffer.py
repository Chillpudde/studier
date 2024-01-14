# 2.05: Finn ut om siste siffer er felles

a = 48
b = 168
c = 3518

# Modulus (%) returns the reminder of the division

if a%10 == b%10:
    print(f'Siste siffer i {a} og {b} er like.')
if a%10 == c%10:
    print(f'Siste siffer i {a} og {c} er like.')
if b%10 == c%10:
    print(f'Siste siffer i {b} og {c} er like.')
if a%10 == b%10 and a%10 == c%10 and b%10 == c%10:
    print(f'Siste siffer i {a}, {b} og {c} er like.')
