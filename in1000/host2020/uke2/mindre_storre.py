# 02.06: Mindre eller større enn

x = int(input("Tast inn et tall: "))

"""
if (x < 10):
    print("Tallet er under 10")
elif (x > 10):
    print("Tallet er over 10")
else:
    print("Tallet du skrev inn er 10")

if (x < 20):
    print("Tallet er under 20")
elif (x > 20):
    print("Tallet er over 20")
else:
    print("Tallet du skrev inn er 20")
"""

if (x < 10):
    print("Tallet er under 10")
elif (x > 20):
    print("Tallet er over 20")
elif (x == 10 or x == 20):
    print("Tallet er", x)
else:
    print("Tallet er mellom 10 og 20")
