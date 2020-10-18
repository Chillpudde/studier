# 02.16: Skatt i Ruritania

inntekt = float(input("Din inntekt: "))
skatt = 0

if (inntekt < 10000):
    skatt = inntekt * 0.1
else:
    skatt = (10000 * 0.1) + ((inntekt - 10000) * 0.3)

print("Din skatt:", skatt)
