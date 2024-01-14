# 02.15: Feil i små program

tall = float(input("Tast inn et siffer: "))
dobbelt = 2 * tall
print("Det dobbelte er ", dobbelt)

"""
Linje 3, leste ikke inn som float (eller int) | mangle "" rundt tekst
Linje 5, manglet "," etter tekst | skrivefeil dobbel, ikke dobbelt
"""