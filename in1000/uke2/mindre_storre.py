# 2.06: Mindre eller større enn


tall = int(input("Tast inn et tall: "))

if tall < 10:
    print("Tallet er mindre enn 10.")
elif tall == 10:
    print("Tallet er lik 10.")
elif tall > 20:
    print("Tallet er større enn 20.")
elif tall > 10 and tall < 20:
    print("Tallet er mellom 10 og 20.")
else:
    print("Tallet er større enn 10.")
