# 02.07: Sannhetsverdier

"""
Gitt at verdien av b er False,
og verdien av x er 0, hva er sannhetsverdien til følgende uttrykk?
"""

b = False
x = 0

# a)
e = bool(b) # False

# b)
f = bool(x == 0) # True

# c)
g = b and x == 0 # False

# d)
h = b or x == 0 # True

# e)
i = not b and x == 0 # True

# f)
j = not b or x == 0 # True

# g)
k = b and x != 0 # False

# h)
l = b or x != 0 # False

# i)
i = not b and x != 0 # False

# j)
j = not b or x != 0 # True

print(j)