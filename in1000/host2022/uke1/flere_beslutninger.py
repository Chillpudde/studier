# 01.13 Flere beslutninger

# a)
a = 6

if 6 == a:
    print("IN1000")
# a er definert som 6, skrives ut

# b)
a = 5
b = 6

if a > b:
    print("IN1000")
# a er 5 og b er 6. a er ikke større enn 5, skrives ikke ut

# c)
a = 5 + 2
b = 6

if a <= b:
    print("IN1000")
# a blir 7, b er ikke mindre enn eller lik 7, skrives ikke ut

# d)
a = 6
b = a

if a >= b:
    print("IN1000")
# a er 6, b er samme som a, skrives ut

# e)
a = 6 + 1

if a == a:
    print("ingenting")
else:
    print("IN1000")
# a er 7, a har samme verdi som a. "ingenting" skrives ut. Ikke "IN1000"
