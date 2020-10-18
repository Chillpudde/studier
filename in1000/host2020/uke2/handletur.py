# 02.18: handletur

pris_brod = 20
pris_melk = 15
pris_ost = 40
pris_yoghurt = 12

sum = 0

print("| HANDLETUR | \n")

ant_brod = int(input("Hvor mange brod vil du ha?: "))
sum += ant_brod * pris_brod # += legger til verdien av variabelen "ant_brod"

ant_melk = int(input("Hvor mange melk vil du ha?: "))
sum += ant_melk * pris_melk

ant_ost = int(input("hvor mange ost vil du ha?: "))
sum += ant_ost * pris_ost

ant_yoghurt = int(input("Hvor mange yoghurt?: "))
sum += ant_yoghurt * pris_yoghurt

print()
print("Handleturen kostet:", sum, "kr")
