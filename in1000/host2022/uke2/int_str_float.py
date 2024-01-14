# 02.02: int, str, float

# Hva skrives ut?

# a)
print(type(3))
# "int" skrives ut

# b)
print(type("3"))
# "str" skrives ut

# c)
print(type(5.0 + 3.5))
# "float" skrives ut

# d)
print(float("4" + ".8") / 2)
# "2.4" skrives ut, da float ber om at det skal tolkes som
# desimaltall

# e)
print("3" + "5")
# "35" skrives ut

# f)
print("3"*3)
# "333" skrives ut. Gjentar str tre ganger

# g)
print(type(3*"A"))
# "str" skrives ut, da dette tolkes som tre ganger repetisjon av en str

# h)
print(type(int("3")))
# "int" skrives ut. 3 konverteres til int, ber deretter om type

# i)
# print(3 + "3")
# "error", kan ikke kombinere int og str

# j)
print(float(3))
# "3.0". Int tolkes som float, legger til en desimal og .

# k)
print("1.50" == "1.5")
# "false", booleansk sjekk av at verdiene er helt identiske

# l)
print(float("1.50") == float("1.5"))
# "true", begge konverteres til float, 0 sløyfes fra første del