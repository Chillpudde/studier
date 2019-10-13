# 2.07: Skatt i Ruritania

brutto_inntekt = float(input("Skriv inn inntekten din: "))
skatt = 0.0

if brutto_inntekt < 10000:
    skatt = brutto_inntekt*0.10
    print(f'Skatt: {skatt}')
if brutto_inntekt >= 10000:
    skatt = ((brutto_inntekt-10000)*0.3)+(10000*0.1)
    print(f'Skatt: {skatt}')
