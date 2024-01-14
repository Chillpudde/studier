# 02.16: Skatt i Ruritania

inntekt = float(input("Inntekt: "))
skatt = 0


if inntekt < 10000:
    skatt = inntekt * 0.1
    print("Skatt: ", skatt)

if inntekt >= 10000:
    skatt = (10000 * 0.1)+((inntekt-10000)*0.3)
    print("Skatt: ", skatt)
