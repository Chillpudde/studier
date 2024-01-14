# 02.07: Sannhetsverdier

"""
Gitt at verdien av b = false, og verdien av x = 0.
Hva er sannhetsverdien til følgende uttrykk?
"""

b = False
x = 0

print("1.", bool(b)) # false

print("2.", bool(x == 0)) # true

print("3.", bool(b and x == 0)) # false

print("4.", bool(b or x == 0)) # (Semikolon? Python prøver å leke java. Ellers true)

print("5.", bool(not b and x == 0)) # true

print("6.", bool(not b or x == 0)) # true

print("7.", bool(b and x != 0)) # false

print("8.", bool(b or x != 0)) # false

print("9.", bool(not b and x != 0)) # false

print("10.", bool(not b or x != 0)) # true
