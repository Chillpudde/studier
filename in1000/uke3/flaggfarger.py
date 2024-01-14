# 03.13: Flaggfarger

flaggOrdbok = {"norge" : ["rodt", "hvitt", "blaatt"],
"sverige" : ["blaatt", "gult"],
"danmark" : ["rodt", "hvitt"],
"finland" : ["hvitt", "blaatt"],
"japan" : ["rodt", "hvitt"],
"gabon" : ["gront", "gult", "blaatt"],
"storbritannia" : ["rodt", "blaatt", "hvitt"],
"chile" : ["blaatt", "hvitt", "rodt"]
}

"""
# a)
for land in flaggOrdbok:
    print(land + ": " + str(flaggOrdbok[land]))

# b)
flaggOrdbok["usa"] = ["rodt", "hvitt", "blaatt"]
print("\n")

for land in flaggOrdbok:
    print(land + ": " + str(flaggOrdbok[land]))
"""

# c)

def flaggfarger():
    land = input("Hvilket land vil du se fargene til?: ")
    if land in flaggOrdbok:
        print(land + ": " + str(flaggOrdbok[land]))
    else:
        print("Ugyldig valg!")

flaggfarger()
