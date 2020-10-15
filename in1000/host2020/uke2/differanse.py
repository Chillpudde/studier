# 02.03: Differansen mellom to heltall

print("| Skriv inn to heltall | \n")

# int() sikrer at verdien som oppgis regnes som et heltall
x = int(input("Oppgi verdien til x: "))
y = int(input("Oppgi verdien til y: "))

print("Differansen mellom x og y er", x-y)

# For å finne absoluttverdien kan man legge inn "x-y" som argument i funksjonen
# "abs()"

print("Differansen/absoluttverdien mellom x og y er", abs(x-y))
