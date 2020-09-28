# 01.11: Utskrift med formatering

lengde = 10.101
bredde = 3.843

"""
Her tolkes lengde og bredde som tekst, ved å hente inn variablene i print
med bruk av "{}". ":.xf" brukes for å definere antall desimaler som skal tas
med i utskriften.
"""

print(f'Rektangelet er {lengde:.1f} cm langt og {bredde:.1f} cm bredt.')

# Eventuelt kan man bruke matte-funksjonen "round()"
print("Rektangelet er", round(lengde, 1), "cm langt og",
    round(bredde, 1), "cm bredt.")
