# Oppgave 2. Konvertering

temp_f = float(input("Oppgi temperaturen i fahrenheit: ")) # fahrenheit
print(f"Temperaturen er {temp_f}F")

omregning = "{:.2f}".format((temp_f-32)*(5/9))

print(f"Temperaturen i celcius er: {omregning}C")
