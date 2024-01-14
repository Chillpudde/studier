# 02.06: Differansen mellom to tall

def les_inn():
    x = int(input("X: "))
    y = int(input("y: "))

    diff = abs(x-y)
    print("Differansen mellom %.0f og %.0f er: %.0f" % (x, y, diff))

les_inn()