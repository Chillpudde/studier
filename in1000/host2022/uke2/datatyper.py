# 02.03: Input og datatyper

# a), b), c)

"""
a = input("Skriv inn en str: ")
b = int(input("Skriv inn en int: "))
c = float(input("Skriv inn en float: "))

print(type(a))
print(type(b))
print(type(c))

"""

# i) OK
# ii) OK, 3 blir 3.0
# iii) -0 blir 0
# iv) ERROR, kan ikke konvertere 3.8 til int

# d)
# i) int*str, repeterer str a ganger
# ii) Gir float
# iii) ERROR, kan ikke multiplisere float
# og str

"""
d = "test"

print(e*d)
"""
e = 3.9999

# e)

f = int(e)
print(f)

# Dersom man forsøker å konvertere float til int blir kun venstre siden av
# komma tatt med aka rundet ned til nærmeste heltall