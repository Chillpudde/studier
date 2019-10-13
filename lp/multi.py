# 1.6 Functions: Problem 7

def square(x):
    return x * x

print(square(5))

def sum_of_squares(x, y):
    return square(x) + square(y)

print(sum_of_squares(2, 3))

f = square
print(f(4))

def fxy(f, x, y):
    return f(x) + f(y)

a = fxy(square, 2, 3)

print(a)
